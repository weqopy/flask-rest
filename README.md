# flask-rest

An example for RESTful APIs.

Follows [this site](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)

---
## APIs:
### **v1.0**
```
# first api, get_tasks
curl -i http://localhost:5000/todo/api/v1.0/tasks
# second api, get_task
curl -i http://localhost:5000/todo/api/v1.0/tasks/2
# third api, create_task
curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000/todo/api/v1.0/tasks
# forth api, update_task
curl -i -H "Content-Type: application/json" -X PUT -d '{"done":true}' http://localhost:5000/todo/api/v1.0/tasks/2
# fifth api, delete_task
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/api/v1.0/tasks/2
```
### **v1.1**
```
# security auth
curl -u root:1230 -i http://localhost:5000/todo/api/v1.0/tasks
```
