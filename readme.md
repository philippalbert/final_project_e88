# Final project

## Twitter api

### Credentials

API Key: 

HgMMUUfCy4gyHZ5ZOCSNQIZFw

API secret key: 

h4i3qOeP1LE9Zhn98AKrfdz7zkOUyD3kigFwO1tkny1eXrutkM

Bearer Token: 
AAAAAAAAAAAAAAAAAAAAACddbwEAAAAAGvQkwOi2nLiYVK0IzBSJGFSPVPE%3DlAd4BYPwtci40JmNPtYp9bPx0xCOxSuRemQvYj54qbod5Fuz0e

## Grafana

traces:
  configs:
  - name: default
    remote_write:
      - endpoint: tempo-us-central1.grafana.net:443
        basic_auth:
          username: 198548
          password: eyJrIjoiMzcwYmZjNWNhNmFiNjE1M2ZkMDMzYTE3ZmQ1MDEwNDZjMGYxNjFmMSIsIm4iOiJwaGlsaXBwX3VidW50dV9sb2NhbCIsImlkIjo2MzY1MjN9

receivers:
  jaeger:
    protocols:
      grpc:
      thrift_binary:
      thrift_compact:
      thrift_http:
  zipkin:
  otlp:
    protocols:
      http:
      grpc:
  opencensus: