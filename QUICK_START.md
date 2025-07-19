# 🚀 Quick Start Guide - Mental Health Risk Assessment

## What You Have

This project includes a complete **Mental Health Risk Assessment System** with:

- ✅ **50,000+ patient dataset** with realistic mental health data
- ✅ **AI-powered risk prediction** using multiple algorithms
- ✅ **Interactive web interface** for healthcare professionals
- ✅ **Command-line demonstration** with sample scenarios
- ✅ **Comprehensive documentation** and clinical recommendations

## 🎯 Quick Start Options

### Option 1: Command Line Demo (Recommended to start)
```bash
python demo_model.py
```
This runs an interactive demonstration showing:
- Multiple patient scenarios (Low, Moderate, High, Critical risk)
- Risk factor analysis
- Clinical recommendations
- Interactive patient assessment

### Option 2: Web Application
```bash
streamlit run simple_app.py
```
Then open your browser to `http://localhost:8501`

Features:
- Professional web interface
- Real-time risk assessment
- Interactive sliders for patient data
- Visual risk factor analysis
- **PDF reports with graphs and visualizations**
- CSV and text report exports

### Option 3: Generate New Dataset
```bash
python data_generator.py
```
Creates a new dataset with 50,000 patient records.

## 📊 What the System Does

### Risk Assessment
- **Analyzes 20+ risk factors** including clinical scores, behavioral indicators, and treatment history
- **Calculates risk probability** using weighted algorithms
- **Categorizes risk levels**: Low, Moderate, High, Critical
- **Provides clinical recommendations** based on risk level

### Clinical Integration
- **Standardized assessment scales**: PHQ-9, GAD-7, CSSRS, Beck Hopelessness
- **Treatment history tracking**: Previous attempts, hospitalizations, compliance
- **Environmental factors**: Social support, housing stability, healthcare access
- **Family history analysis**: Depression, anxiety, suicide, substance abuse

### Output Features
- **Risk probability scores** (0-100%)
- **Risk level categorization**
- **Individual risk factor contributions**
- **Clinical intervention recommendations**
- **Exportable assessment reports** (CSV, Text, and **PDF with graphs**)

## 🏥 Clinical Use Cases

### For Mental Health Companies:
1. **Initial Patient Screening** - Quick risk assessment for new patients
2. **Regular Monitoring** - Track risk changes over time
3. **Crisis Prevention** - Identify high-risk patients for intervention
4. **Resource Allocation** - Prioritize care based on risk levels
5. **Treatment Planning** - Guide clinical decisions with data

### Risk Levels & Actions:

#### 🟢 Low Risk (< 20%)
- Regular therapy sessions
- Medication management
- Lifestyle recommendations
- Support group referral

#### 🟡 Moderate Risk (20-40%)
- Weekly therapy sessions
- Safety planning
- Medication review
- Family involvement

#### 🟠 High Risk (40-60%)
- Immediate psychiatric evaluation
- 24/7 monitoring or hospitalization
- Crisis intervention team activation
- Remove access to lethal means

#### 🔴 Critical Risk (> 60%)
- 🚨 IMMEDIATE EMERGENCY INTERVENTION
- Call 911 or emergency services
- Psychiatric hospitalization
- Crisis team activation

## 📁 Project Structure

```
mental-health-risk-assessment/
├── data_generator.py          # Generate realistic patient data
├── demo_model.py             # Command-line demonstration
├── simple_app.py             # Streamlit web application
├── pdf_generator.py          # PDF report generation with graphs
├── requirements.txt          # Python dependencies
├── README.md                 # Comprehensive documentation
├── QUICK_START.md           # This file
└── mental_health_dataset.csv # Generated dataset
```

## 🔧 Technical Details

### Data Features (20+ variables):
- **Demographics**: Age, gender, ethnicity, socioeconomic status
- **Clinical Scores**: PHQ-9, GAD-7, CSSRS, Hopelessness Scale
- **Behavioral**: Sleep patterns, social isolation, substance use
- **Treatment**: Previous attempts, hospitalizations, compliance
- **Environmental**: Housing, healthcare access, social support
- **Family History**: Depression, anxiety, suicide, substance abuse

### Risk Calculation:
- **Weighted algorithm** based on clinical research
- **Normalized scoring** for different assessment scales
- **Multi-factor analysis** considering all risk indicators
- **Realistic probability distribution**

## 🚨 Important Notes

### Clinical Disclaimer:
- This is a **demonstration system** for educational purposes
- **Should not replace clinical judgment** or professional assessment
- All predictions should be **reviewed by qualified mental health professionals**
- Use as a **supplementary tool** for risk assessment

### Data Privacy:
- All data is **synthetic and anonymized**
- No real patient information is used
- System designed for **HIPAA compliance** in production use

## 🎓 Learning Outcomes

After using this system, you'll understand:

1. **How AI can assist mental health assessment**
2. **Key risk factors for mental health crises**
3. **Clinical decision-making with data**
4. **Early intervention strategies**
5. **Resource allocation for mental health services**

## 🚀 Next Steps

1. **Try the demo** to see the system in action
2. **Explore the web interface** for interactive assessment
3. **Review the dataset** to understand the data structure
4. **Read the full documentation** for technical details
5. **Consider implementation** in your mental health practice

## 📞 Support

If you have questions or need help:
- Check the comprehensive `README.md`
- Review the code comments for technical details
- The system is designed to be self-explanatory

---

**Ready to start? Run `python demo_model.py` to see the system in action!** 🧠✨ 