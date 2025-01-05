kubectl patch app -n argocd 2games1helm  -p '{"metadata": {"finalizers": ["resources-finalizer.argocd.argoproj.io"]}}' --type merge
kubectl delete app -n argocd 2games1helm