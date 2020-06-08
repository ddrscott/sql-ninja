FROM python:3-alpine

RUN pip install sql-ninja

ENTRYPOINT ["/usr/local/bin/sql"]

CMD ["--help"]
