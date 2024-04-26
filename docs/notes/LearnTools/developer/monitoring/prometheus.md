# Prometheus

https://prometheus.io/

> Monitoring system & time series database

## Introduction

Supports monitoring anything

- App
- Server
- Database

## Metrics Collection

### Pulls over HTTP

Target needs to expose `/metrics` endpoint.

Prometheus calls the endpoint to retrieve metric.

### Exporter

There are things that doesn't natively support the `/metrics` endpoint.

Exporter is an adapter that converts metrics to the format prometheus understands and expose `metrics`.

Exporters are also availble as docker image. For example, to export metrics of a MySQL DB, one can use a side car docker container exporter.

## Config

A yml file is used to specify the targets.

## Data Storage

Supports both local and Remote Storage.

## Query

- Use language `PromQL` on Prometheus Web UI and get metric data.
- Use data visualization tools like Grafana

Example `PromQL`

```
# All HTTP status codes except 4xx ones
http_requests_total{status!~"4.."}

# 5-min rate of `http_requests_total` for the past 30 mins
rate(http_requests_total[5m])[30m:]
```

## Alert

Alerts are defined by rules. Alertmanager is responsible for pushing alerts, email, slack, etc.

## Reference

- [YouTube: How Prometheus Monitoring works | Prometheus Architecture explained](https://youtu.be/h4Sl21AKiDg)
- [Setup Prometheus Monitoring on Kubernetes using Helm and Prometheus Operator | Part 1](https://youtu.be/QoDqxm7ybLc)
