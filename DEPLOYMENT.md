# 🚀 Deployment Guide - Mental Health Risk Assessment

## Quick Deployment Options

### **Option 1: Streamlit Cloud (Recommended - Free)**

**Steps:**
1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/mental-health-risk-assessment.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file path: `simple_app.py`
   - Click "Deploy"

**✅ Pros:** Free, automatic updates, no server management
**❌ Cons:** Limited resources, public by default

---

### **Option 2: Docker Deployment**

**Local Docker:**
```bash
# Build and run with Docker
docker build -t mental-health-app .
docker run -p 8501:8501 mental-health-app
```

**Docker Compose:**
```bash
# Start with Docker Compose
docker-compose up -d

# Access at: http://localhost:8501
```

**Cloud Docker (AWS/GCP/Azure):**
```bash
# Build and push to container registry
docker build -t your-registry/mental-health-app .
docker push your-registry/mental-health-app

# Deploy to cloud container service
```

---

### **Option 3: Heroku Deployment**

**Steps:**
1. **Create Procfile:**
   ```
   web: streamlit run simple_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku open
   ```

---

### **Option 4: AWS/GCP/Azure Cloud**

**AWS EC2:**
```bash
# Launch EC2 instance
# Install Docker
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo usermod -a -G docker ec2-user

# Deploy app
docker-compose up -d
```

**Google Cloud Run:**
```bash
# Build and deploy
gcloud builds submit --tag gcr.io/YOUR_PROJECT/mental-health-app
gcloud run deploy --image gcr.io/YOUR_PROJECT/mental-health-app --platform managed
```

---

## 🔧 Environment Setup

### **Production Requirements:**
- Python 3.8+
- 2GB RAM minimum
- 1GB storage
- HTTPS enabled (for production)

### **Environment Variables:**
```bash
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

---

## 📊 Monitoring & Maintenance

### **Health Checks:**
- App health: `http://your-domain:8501/_stcore/health`
- Status page: `http://your-domain:8501/_stcore/status`

### **Logs:**
```bash
# Docker logs
docker logs mental-health-app

# Streamlit logs
streamlit run simple_app.py --logger.level=info
```

### **Updates:**
```bash
# Pull latest changes
git pull origin main

# Rebuild and restart
docker-compose down
docker-compose up -d --build
```

---

## 🔒 Security Considerations

### **Production Security:**
1. **HTTPS Only** - Use SSL certificates
2. **Authentication** - Add login system if needed
3. **Rate Limiting** - Prevent abuse
4. **Data Privacy** - Ensure HIPAA compliance
5. **Backup** - Regular data backups

### **Security Headers:**
```python
# Add to simple_app.py
st.set_page_config(
    page_title="Mental Health Risk Assessment",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Security headers
st.markdown("""
<meta http-equiv="Content-Security-Policy" content="default-src 'self'">
""", unsafe_allow_html=True)
```

---

## 📈 Scaling Options

### **Horizontal Scaling:**
```yaml
# docker-compose.yml with multiple instances
services:
  mental-health-app:
    deploy:
      replicas: 3
    ports:
      - "8501-8503:8501"
```

### **Load Balancer:**
```nginx
# nginx.conf
upstream streamlit {
    server localhost:8501;
    server localhost:8502;
    server localhost:8503;
}

server {
    listen 80;
    location / {
        proxy_pass http://streamlit;
    }
}
```

---

## 🚨 Troubleshooting

### **Common Issues:**

**Port Already in Use:**
```bash
# Find and kill process
lsof -ti:8501 | xargs kill -9
```

**Memory Issues:**
```bash
# Increase Docker memory
docker run -m 4g mental-health-app
```

**PDF Generation Fails:**
```bash
# Install system fonts
apt-get install -y fonts-liberation
```

---

## 📞 Support

### **Deployment Help:**
- Check logs: `docker logs <container_name>`
- Verify ports: `netstat -tulpn | grep 8501`
- Test connectivity: `curl http://localhost:8501`

### **Resources:**
- [Streamlit Deployment](https://docs.streamlit.io/streamlit-community-cloud)
- [Docker Documentation](https://docs.docker.com/)
- [Heroku Documentation](https://devcenter.heroku.com/)

---

## 🎯 Recommended Deployment Path

1. **Development:** Local Streamlit
2. **Testing:** Streamlit Cloud (free)
3. **Production:** Docker on cloud provider
4. **Enterprise:** Kubernetes cluster

**Ready to deploy? Choose your preferred option above!** 🚀 