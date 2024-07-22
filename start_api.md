
## 启动API服务

```shell
cd api
flask run --host 0.0.0.0 --port=5001 --debug
```

## 启动Worker服务

- windows系统
```shell
cd api
celery -A app.celery worker -P solo --without-gossip --without-mingle -Q dataset,generation,mail,ops_trace --loglevel INFO
```

- Linux系统
```shell
cd api
celery -A app.celery worker -P gevent -c 1 -Q dataset,generation,mail,ops_trace --loglevel INFO
```