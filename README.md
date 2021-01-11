My First DAG
------------
This is my first DAG created to play with airflow.

### How to run?

Install docker if you don't have one. Get the container of airflow, I have used ***puckel/docker-airflow***.

```sh
docker pull puckel/docker-airflow
```

Check if you have the image now

```sh
docker images
```

Now you can run the image

```sh
docker run -d -p 8080:8080 puckel/docker-airflow webserver
```

Airflow dashboard can be found visiting http://localhost:8080/admin/

Check the docker name by

```sh
docker ps
```

Stop this if you want by

```sh
docker stop <container name>
```

So your container is up and running. Now, how do we start defining DAGs?

Create the python DAG file and then give the path of that file while running again

```sh
docker run -d -p 8080:8080 -v /path/to/dags/on/your/local/machine/:/usr/local/airflow/dags  puckel/docker-airflow webserver
```

Hope that helps!
