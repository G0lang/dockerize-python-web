# dockerize-python-web
Try to dockerize python web application with different solutions




1. gunicorn 


- test result with 
    ```
	$ ./go-wrk -c 80 -d 5  http://localhost:8080
	Running 5s test @ http://localhost:8080
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
