# Kubernetes deployment with kubectl

This is a kubectl-first version of the original `README.md`.

It assumes:

- you already have a Kubernetes cluster running
- `kubectl` is configured to point to that cluster
- you are **not** using `minikube`

Check first:

```bash
kubectl config current-context
kubectl get nodes
```

If those work, continue.

---

## Files

- `backend.yaml` — Deployment + NodePort Service for the FastAPI backend
- `frontend.yaml` — Deployment + NodePort Service for the React frontend
- `combined-pod.yaml` — one Pod running both containers + one Service exposing both ports

These manifests use:

```yaml
imagePullPolicy: Never
```

That means Kubernetes will not pull images from a registry. The images must already exist in the cluster's runtime.

---

## Before deploying: make the images available to your cluster

Build both images locally:

```bash
docker build -t learning-app-backend:latest ./backend
docker build -t learning-app-frontend:latest ./frontend
```

Then choose the image-loading step that matches your cluster.

### Option 1: Docker Desktop Kubernetes

Usually the Docker-built images are directly usable by the cluster.

If pod startup fails with `ErrImageNeverPull` or `ImagePullBackOff`, switch to Option 2 style and load/push the images explicitly.

### Option 2: kind

Load the images into the kind cluster:

```bash
kind load docker-image learning-app-backend:latest
kind load docker-image learning-app-frontend:latest
```

### Option 3: other local/remote clusters

If your cluster cannot see your local Docker images, push them to a registry and update the manifests:

- change `image:` to your registry path
- change `imagePullPolicy: Never` to `IfNotPresent` or `Always`

Example:

```yaml
image: yourname/learning-app-backend:latest
imagePullPolicy: IfNotPresent
```

---

## Path A - separate frontend + backend manifests

```bash
# 1. Apply the manifests
kubectl apply -f k8s/backend.yaml
kubectl apply -f k8s/frontend.yaml

# 2. Watch pods come up
kubectl get pods -w

# 3. Inspect services
kubectl get svc
```

### Access the app

For local development, port-forward is the most reliable choice:

```bash
kubectl port-forward svc/frontend 5000:5000
kubectl port-forward svc/backend 8000:8000
```

Then open:

- Frontend: http://localhost:5000
- Backend:  http://localhost:8000/api/hello

Note: keep both port-forward terminals open while testing.

---

## Path B - single multi-container Pod

```bash
# 1. Apply the combined manifest
kubectl apply -f k8s/combined-pod.yaml

# 2. Watch it come up
kubectl get pod learning-app -w
```

### Access the app

```bash
kubectl port-forward pod/learning-app 5000:5000 8000:8000
```

Then open:

- Frontend: http://localhost:5000
- Backend:  http://localhost:8000/api/hello

The frontend fetches `http://localhost:8000/api/hello`, so the backend port-forward must also be active.

---

## Inspect what is running

```bash
kubectl get pod,svc
kubectl describe pod learning-app
kubectl logs learning-app -c backend
kubectl logs learning-app -c frontend
kubectl exec -it learning-app -c backend -- sh
```

If you deployed Path A instead of Path B, use:

```bash
kubectl get deploy,pod,svc
kubectl describe deployment backend
kubectl describe deployment frontend
kubectl logs deployment/backend
kubectl logs deployment/frontend
```

---

## Networking notes

There are three useful cases to keep straight:

### 1. Browser to your laptop

When the React app fetches:

```js
fetch('http://localhost:8000/api/hello')
```

that request runs in your browser, so `localhost` means your laptop, not the Pod.

### 2. Laptop to cluster

`kubectl port-forward` exposes a local port on your machine and tunnels traffic into the Pod or Service.

### 3. Container to container inside one Pod

Containers in the same Pod share a network namespace, so they can reach each other through `localhost`.

If frontend and backend run in separate Pods, they should communicate through a Service such as:

```text
http://backend:8000
```

from inside the cluster.

---

## Delete the app

### Stop port-forwards

Press `Ctrl+C` in the terminal running each port-forward.

### Delete Kubernetes resources

Path B:

```bash
kubectl delete -f k8s/combined-pod.yaml
```

Path A:

```bash
kubectl delete -f k8s/backend.yaml
kubectl delete -f k8s/frontend.yaml
```

Verify cleanup:

```bash
kubectl get pod,svc
```

### Remove local images

```bash
docker rmi -f learning-app-backend:latest learning-app-frontend:latest
```

