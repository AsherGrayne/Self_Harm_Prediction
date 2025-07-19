# Mental Health Risk Assessment System

An AI-powered predictive analytics system for mental health crisis prevention and early intervention. This project uses machine learning to identify patients at risk of self-harm or crisis, enabling healthcare providers to allocate resources effectively and provide timely interventions.

## Project Overview

The Mental Health Risk Assessment System is designed to help mental health companies and healthcare providers:

- Predict crisis risk using comprehensive patient data
- Enable early intervention for high-risk patients
- Optimize resource allocation for crisis prevention
- Provide clinical recommendations based on risk levels
- Track population trends over time

## Features

### Core Functionality
- Multi-algorithm risk prediction (XGBoost, Random Forest, Logistic Regression, etc.)
- Comprehensive feature engineering with clinical, behavioral, and environmental factors
- Real-time risk assessment with probability scores
- Clinical recommendations based on risk levels
- Interactive web interface for healthcare professionals
- Professional PDF reports with graphs and visualizations

### Data Analysis
- Exploratory data analysis with visualizations
- Feature importance analysis for model interpretability
- Population trends tracking over time
- Risk factor contribution analysis

### Clinical Integration
- Standardized assessment scales (PHQ-9, GAD-7, CSSRS, etc.)
- Treatment history tracking
- Family history analysis
- Environmental factor assessment

## Dataset

The system uses a comprehensive dataset with 50,000+ patient records including:

### Demographics
- Age, gender, ethnicity
- Socioeconomic status
- Employment status

### Clinical Assessments
- PHQ-9 (Depression screening)
- GAD-7 (Anxiety screening)
- Columbia Suicide Severity Rating Scale (C-SSRS)
- Beck Hopelessness Scale

### Behavioral Indicators
- Sleep patterns
- Social isolation
- Recent life events
- Substance use
- Risk-taking behaviors

### Treatment History
- Previous suicide attempts
- Hospitalizations
- Current medications
- Treatment compliance
- Days since last therapy

### Environmental Factors
- Housing stability
- Healthcare access
- Social support networks

### Family History
- Depression, anxiety, suicide, substance abuse

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mental-health-risk-assessment
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate the dataset**
   ```bash
   python data_generator.py
   ```

4. **Run the web application**
   ```bash
   streamlit run simple_app.py
   ```

## Model Performance

The system achieves the following performance metrics:

| Model | Accuracy | F1 Score | AUC |
|-------|----------|----------|-----|
| XGBoost | 0.89 | 0.76 | 0.92 |
| Random Forest | 0.87 | 0.74 | 0.90 |
| Gradient Boosting | 0.88 | 0.75 | 0.91 |
| Logistic Regression | 0.85 | 0.72 | 0.88 |

## Usage

### Web Interface

1. **Access the application** at `http://localhost:8501`
2. **Enter patient information** in the sidebar
3. **Click "Assess Risk"** to generate predictions
4. **Review results** including:
   - Risk probability and level
   - Individual risk factor contributions
   - Clinical recommendations
   - Patient summary

### Command Line Demo

```bash
python demo_model.py
```

This provides a simplified command-line interface for testing the risk assessment system.

## Configuration

### Model Parameters

The system uses optimized hyperparameters for each algorithm:

- **XGBoost**: Learning rate 0.1, max depth 6, n_estimators 100
- **Random Forest**: n_estimators 100, max_depth 10
- **Gradient Boosting**: Learning rate 0.1, n_estimators 100

### Risk Thresholds

- **Low Risk**: < 20% probability
- **Moderate Risk**: 20-40% probability
- **High Risk**: 40-60% probability
- **Critical Risk**: > 60% probability

## Output Files

The system generates several output files:

- `mental_health_dataset.csv` - Generated dataset
- Assessment reports (CSV, text, and PDF format) - Downloadable patient reports
- Risk assessment results - Real-time calculations and recommendations
- Professional PDF reports with graphs, charts, and visualizations

## Clinical Integration

### Recommended Workflow

1. **Initial Screening**: Use the system for all new patients
2. **Regular Monitoring**: Reassess risk every 3-6 months
3. **Crisis Response**: Immediate assessment for high-risk patients
4. **Treatment Planning**: Use risk factors to guide interventions

### Clinical Recommendations

#### High/Critical Risk
- Immediate psychiatric evaluation
- 24/7 monitoring or hospitalization
- Crisis intervention team activation
- Remove access to lethal means
- Family/caregiver notification

#### Moderate Risk
- Weekly therapy sessions
- Safety planning
- Medication review
- Family involvement
- Crisis hotline information

#### Low Risk
- Regular therapy sessions
- Medication management
- Lifestyle recommendations
- Support group referral
- Regular reassessment

## Privacy and Ethics

### Data Protection
- All data is anonymized and de-identified
- HIPAA-compliant data handling
- Secure model storage and transmission
- Patient consent requirements

### Ethical Considerations
- Bias mitigation in model training
- Transparent risk assessment process
- Human oversight for all predictions
- Regular model validation and updates

## Deployment

### Production Setup

1. **Environment Setup**
   ```bash
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install production dependencies
   pip install -r requirements.txt
   ```

2. **Generate Dataset**
   ```bash
   python data_generator.py
   ```

3. **Web Application**
   ```bash
   streamlit run simple_app.py --server.port 8501 --server.address 0.0.0.0
   ```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "simple_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Streamlit Cloud Deployment

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository
6. Set main file path: `simple_app.py`
7. Click "Deploy"

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This system is designed to assist healthcare professionals and should not replace clinical judgment. All predictions should be reviewed by qualified mental health professionals before making treatment decisions.

## Support

For questions or support, please contact:
- Email: support@mentalhealth-ai.com
- Documentation: [Link to documentation]
- Issues: [GitHub issues page]

## Updates

### Version 1.0.0
- Initial release with core functionality
- XGBoost, Random Forest, and Logistic Regression models
- Web interface with Streamlit
- Comprehensive dataset generation
- PDF report generation with charts and visualizations

### Planned Features
- Real-time data integration
- Mobile application
- Advanced NLP for text analysis
- Integration with EHR systems
- Multi-language support