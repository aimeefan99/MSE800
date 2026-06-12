# Week8 - Activity 5: Car Rental on Kubernetes

This activity turns the Week 8 `car_rental` Docker example into a small Kubernetes case study.

The original project was an interactive CLI program. For Kubernetes, it has been redesigned as a small web API so it can run as a long-lived service inside a Pod.

## Learning Goal

This activity helps explain:

- how Docker containers become Pods in Kubernetes
- why a `Deployment` is useful for restart and self-healing
- why a `Service` gives stable network access
- why SQLite needs persistent storage through a `PersistentVolumeClaim`
- why this demo uses `replicas: 1` instead of scaling out

## Project Structure

```text
Activity5/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── k8s/
    ├── deployment.yaml
    ├── pvc.yaml
    └── service.yaml
```

## Architecture

```text
User / curl
    |
    v
Service (ClusterIP)
    |
    v
Deployment
    |
    v
Pod
    |
    v
Flask Car Rental API
    |
    v
SQLite database (/data/cars.db)
    |
    v
PersistentVolumeClaim
```

## API Endpoints

- `GET /health` - health check
- `GET /cars` - list all cars
- `POST /cars` - add a new car
- `DELETE /cars/<plate>` - remove a car

## Run Locally with Python

```bash
cd MSE800-PSD/Week8/Activity5
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then test:

```bash
curl http://127.0.0.1:8000/health

curl http://127.0.0.1:8000/cars

curl -X POST http://127.0.0.1:8000/cars \
  -H "Content-Type: application/json" \
  -d '{"plate":"ABC123","car_type":"SUV","year":2022}'

curl http://127.0.0.1:8000/cars

curl -X DELETE http://127.0.0.1:8000/cars/ABC123
```

## Build with Docker

```bash
cd MSE800-PSD/Week8/Activity5
docker build -t car-rental-api:latest .
docker run --rm -p 8000:8000 car-rental-api:latest
```

## Deploy to Kubernetes

Before applying the manifests, make sure the image is available to your cluster.

### Option 1: Docker Desktop Kubernetes

Build the image locally:

```bash
docker build -t car-rental-api:latest .
```

### Option 2: kind

```bash
docker build -t car-rental-api:latest .
kind load docker-image car-rental-api:latest
```

### Option 3: Minikube

```bash
docker build -t car-rental-api:latest .
minikube image load car-rental-api:latest
```

### Apply the manifests

```bash
kubectl apply -f k8s/pvc.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Check the resources

```bash
kubectl get pods
kubectl get svc
kubectl get pvc
```

### Access the API

```bash
kubectl port-forward service/car-rental-service 8000:80
```

Open a new terminal and test:

```bash
curl http://127.0.0.1:8000/health

curl -X POST http://127.0.0.1:8000/cars \
  -H "Content-Type: application/json" \
  -d '{"plate":"XYZ789","car_type":"Sedan","year":2021}'

curl http://127.0.0.1:8000/cars
```

## Why `replicas: 1`?

This demo uses SQLite, which stores data in a single local file. That is good for a classroom demonstration, but it is not ideal for multi-replica scaling.

If we scale this application to multiple Pods, each Pod may not safely share the SQLite database in a realistic production setup. So for class:

- Docker shows container packaging
- Kubernetes shows orchestration concepts
- SQLite keeps the example simple

For a real production system, a separate database such as PostgreSQL would be a better design.

## Suggested Class Presentation Flow

### 1. Start from the original Docker example

Explain that the earlier `car_rental` project already runs in Docker, but it is a CLI app and not a service.

### 2. Explain the redesign

Show that Kubernetes works best with long-running services, so the app was changed into a Flask API.

### 3. Explain each Kubernetes object

- `Deployment`: manages the Pod and restarts it if needed
- `Service`: provides stable access to the Pod
- `PersistentVolumeClaim`: keeps `cars.db` even if the Pod restarts

### 4. Do a live demo

1. `kubectl apply -f k8s/`
2. `kubectl get pods,svc,pvc`
3. `kubectl port-forward service/car-rental-service 8000:80`
4. `curl` add a car
5. `curl` list cars
6. Explain where the data is stored

### 5. End with the key lesson

Docker packages one application.

Kubernetes manages how that application runs, restarts, connects, and stores data across a cluster.

## Key Talking Points

- Docker is about containerizing the app.
- Kubernetes is about orchestrating the container.
- Pods are ephemeral, so data persistence matters.
- Services decouple clients from changing Pod IP addresses.
- Health probes help Kubernetes know whether the app is working.
