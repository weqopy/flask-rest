# flask-rest

An example for RESTful APIs.

Follows [this site](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) and [this site](http://www.pythondoc.com/flask-restful/index.html#)

## APIs:
### **v1.0**
| HTTP 方法 | URL                                             | 动作         |
| --------- | ----------------------------------------------- | ------------ |
| GET       | http://localhost:5000/todo/api/v1.0/tasks           | 检索任务列表 |
| GET       | http://localhost:5000/todo/api/v1.0/tasks/[task_id] | 检索某个任务 |
| POST      | http://localhost:5000/todo/api/v1.0/tasks           | 创建新任务   |
| PUT       | http://localhost:5000/todo/api/v1.0/tasks/[task_id] | 更新任务     |
| DELETE    | http://localhost:5000/todo/api/v1.0/tasks/[task_id] | 删除任务     |

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
### **v2.0**
| HTTP 方法 | URL                                             | 动作         |
| --------- | ----------------------------------------------- | ------------ |
| GET       | http://localhost:5000/todo/api/v2.0/tasks           | 检索任务列表 |
| GET       | http://localhost:5000/todo/api/v2.0/tasks/[task_id] | 检索某个任务 |
| POST      | http://localhost:5000/todo/api/v2.0/tasks           | 创建新任务   |
| PUT       | http://localhost:5000/todo/api/v2.0/tasks/[task_id] | 更新任务     |
| DELETE    | http://localhost:5000/todo/api/v2.0/tasks/[task_id] | 删除任务     |

### **v3.0**
| HTTP 方法 | URL                                             | 动作         |
| --------- | ----------------------------------------------- | ------------ |
| POST      | http://localhost:5000/todo/api/v3.0/users           | 注册新用户   |
| GET      | http://localhost:5000/todo/api/v3.0/resource           | 获取资源   |
| GET      | http://localhost:5000/todo/api/v3.0/token           | 创建认证令牌   |

```
# register new user
curl -i -X POST -H "Content-Type:application/json" -d '{"username":"admin", "password":"qwe1230"}' http://127.0.0.1:5000/api/v3.0/users
# get resource by password
curl -u admin:qwe1230 -i -X GET http://localhost:5000/api/v3.0/resource
# create token
curl -u admin:qwe1230 -i -X GET http://localhost:5000/api/v3.0/token
# get resource by token
curl -u token:unused -i -X GET http://localhost:5000/api/v3.0/resource
```
