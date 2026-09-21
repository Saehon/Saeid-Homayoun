FROM python:3.11-slim

LABEL org.opencontainers.image.title="NAAIL OpenLab Prototype 003"
LABEL org.opencontainers.image.description="Evidence-governed public deterministic audit benchmark with a mandatory Human Approval Gate"
LABEL org.opencontainers.image.source="https://github.com/Saehon/Saeid-Homayoun"
LABEL org.opencontainers.image.licenses="SEE LICENSE IN REPOSITORY"
LABEL org.opencontainers.image.version="0.2.3"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN addgroup --system naail \
    && adduser --system --ingroup naail naail \
    && mkdir -p /app/outputs \
    && chown -R naail:naail /app

USER naail

ENTRYPOINT ["python", "prototype003.py"]
