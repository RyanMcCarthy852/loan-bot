# LLM Tomfoolery
Goal: Make a loan company chatbot.

### Next Steps
* Use retrieval augmented generation (RAG) to make LLM pull from specific datasources
* make it use GPU and not horribly slow


### Run/Develop
* spin up minikube
* deploy manifests.yaml 
* run application

```
minkube start
kubectl config use-context minikube
```

Run App
```
cd app
python3 -m venv .venv
pip3 install . 
source .venv/bin/activate
source .venv/Scripts/activate # ew

writer run app
```

Interactive edit mode
```
writer edit app
```
