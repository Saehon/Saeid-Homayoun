"""Fast local checks of V6 data-contract and chronology; real-source QA runs in CI."""
import io,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np,pandas as pd,pytest
from build_panel import (SIGNAL_MAP,read_snapshot,read_ff5,select_spec,tidy_chunk,no_future_features,audit)

def synthetic():
    dates=pd.date_range('2020-01-01','2025-12-01',freq='MS')
    return pd.DataFrame({k:np.linspace(-.01,.02,len(dates)) for k in SIGNAL_MAP},index=dates)

def test_lag_features_never_expose_current_or_future_outcome():
    p=synthetic();q=no_future_features(p,['BM'])
    assert np.isnan(q.iloc[0,0])
    assert q.iloc[1,0]==pytest.approx(p.iloc[0]['BM'])
    z=p.copy();z.iloc[25, list(p).index('BM')]=300.0
    assert q.iloc[25,0]==pytest.approx(no_future_features(z,['BM']).iloc[25,0])

def test_data_quality_duplicate_rejected():
    p=synthetic();q=pd.concat([p,p.iloc[[0]]]);
    with pytest.raises(ValueError):audit(q,list(SIGNAL_MAP))

def test_data_quality_full_months():
    p=synthetic();q=audit(p,list(SIGNAL_MAP));assert q['months_expected']==60 and q['months_present']==60 and q['missing_months']==0

def test_tidy_chunks_correct():
    assert tidy_chunk(1)=='id_0000001-0001000.parquet'
    assert tidy_chunk(1001,'costs/')=='costs/id_0001001-0002000.parquet'

def test_predeclared_eight_signals():
    assert len(SIGNAL_MAP)==8 and len(set(SIGNAL_MAP.values()))==8

def test_selection_independent_of_row_order():
    # All columns used by deterministic choice; no return/outcome column is permitted
    base={'id':[200,100], 'sorting_method':['univariate','univariate'],
          'weighting_scheme':['VW','VW'],'rebalancing':['monthly','monthly'],
          'breakpoints_exchanges':['NYSE','NYSE'],'sorting_variable_lag':['ff','ff'],
          'n_portfolios_main':[5,5], 'min_size_quantile':[np.nan,np.nan],
          'exclude_financials':[False,False],'exclude_utilities':[False,False],
          'exclude_negative_book_equity':[False,False],'exclude_negative_earnings':[False,False]}
    g=pd.DataFrame(base)
    assert select_spec(g)['id']==100
    assert select_spec(g.iloc[::-1])['id']==100

def test_return_unit_conversion_and_sort():
    p=pd.DataFrame({'date':['2024-02-29','2024-01-31'],**{k:[1.0,-2.0] for k in SIGNAL_MAP}})
    b=io.BytesIO();p.to_parquet(b)
    a=read_snapshot(b.getvalue());assert a.index.is_monotonic_increasing
    assert a.loc['2024-01-01','BM']==pytest.approx(-0.02)

def test_source_vintage_proof_not_inferred_from_feature_lag():
    q=no_future_features(synthetic(),['BM']);assert q.shape[1]==1
    # PIT availability is a distinct, manual gate; mathematical shift alone never certifies it.
