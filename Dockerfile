FROM python:3-alpine

RUN pip install sql-ninja==0.1.4

ENTRYPOINT ["/usr/local/bin/sql"]

CMD ["--help"]
