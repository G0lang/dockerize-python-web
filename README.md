# dockerize-python-web
Try to dockerize python web application with different solution

1. gunicorn 

- build docker image

    ```
    $ docker build -t gunicorn -f Dockerfile-gunicorn
    ```
- run docker 
    ```
    $ docker run -d -p 80:8080 gunicorn
    ```

- test result with 

    ```
	$ ./go-wrk -c 80 -d 5  http://localhost:80
	Running 5s test @ http://localhost:80
	  80 goroutine(s) running concurrently
	1189 requests in 5.131723889s, 184.62KB read
	Requests/sec:		231.70
	Transfer/sec:		35.98KB
	Avg Req Time:		345.279992ms
	Fastest Request:	81.419954ms
	Slowest Request:	714.153414ms
	Number of Errors:	0
   ```

2. uwsgi 

- build docker image

    ```
    $ docker build -t wsgi -f Dockerfile-wsgi
    ```

- run docker 
    ```
    $ docker run -d -p 80:8080 uwsgi
    ```


- test result 

    ```
       $ ./go-wrk -c 80 -d 5  http://localhost:80
       Running 5s test @ http://localhost:80
       80 goroutine(s) running concurrently
       1235 requests in 5.05482308s, 88.04KB read
       Requests/sec:	        244.32
       Transfer/sec:	        17.42KB
       Avg Req Time:	        327.437932ms
       Fastest Request:	        27.060363ms
       Slowest Request:	        786.284223ms
       Number of Errors:	0
    ```

# TODO

- [ ] add makefile 
- [ ] fix debug mode and pass env variable
- [ ] increse number of worker 


# NOTE

**both service run as www-data user wich is not root user and not allow to use port below than 1024**
