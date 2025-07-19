import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from pdf_generator import MentalHealthPDFGenerator

# Page configuration
st.set_page_config(
    page_title="Mental Health Risk Assessment",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .risk-high {
        color: #d62728;
        font-weight: bold;
    }
    .risk-moderate {
        color: #ff7f0e;
        font-weight: bold;
    }
    .risk-low {
        color: #2ca02c;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

class SimpleRiskAssessment:
    def __init__(self):
        self.risk_weights = {
            'phq9_score': 0.20,
            'gad7_score': 0.15,
            'hopelessness_score': 0.25,
            'cssrs_score': 0.30,
            'previous_suicide_attempts': 0.35,
            'social_isolation': 0.10,
            'substance_use': 0.12,
            'recent_life_events': 0.08,
            'family_suicide': 0.20,
            'treatment_compliance': 0.05
        }
    
    def calculate_risk_score(self, patient_data):
        """Calculate risk score based on patient data"""
        risk_score = 0
        
        for factor, weight in self.risk_weights.items():
            if factor in patient_data:
                # Normalize values based on their ranges
                if factor == 'phq9_score':
                    normalized_value = patient_data[factor] / 27
                elif factor == 'gad7_score':
                    normalized_value = patient_data[factor] / 21
                elif factor == 'hopelessness_score':
                    normalized_value = patient_data[factor] / 20
                elif factor == 'cssrs_score':
                    normalized_value = patient_data[factor] / 25
                elif factor == 'social_isolation':
                    normalized_value = patient_data[factor] / 10
                elif factor == 'substance_use':
                    normalized_value = patient_data[factor] / 10
                elif factor == 'recent_life_events':
                    normalized_value = patient_data[factor] / 8
                elif factor == 'treatment_compliance':
                    normalized_value = (100 - patient_data[factor]) / 100
                else:
                    normalized_value = min(patient_data[factor] / 5, 1)
                
                risk_score += normalized_value * weight
        
        # Add some randomness for realism
        risk_score += np.random.normal(0, 0.05)
        risk_score = max(0, min(1, risk_score))
        
        return risk_score
    
    def determine_risk_level(self, risk_score):
        """Determine risk level based on score"""
        if risk_score < 0.2:
            return "Low"
        elif risk_score < 0.4:
            return "Moderate"
        elif risk_score < 0.6:
            return "High"
        else:
            return "Critical"
    
    def get_recommendations(self, risk_level):
        """Get clinical recommendations based on risk level"""
        recommendations = {
            "Low": [
                "Regular therapy sessions",
                "Medication management",
                "Lifestyle recommendations",
                "Support group referral",
                "Regular reassessment"
            ],
            "Moderate": [
                "Weekly therapy sessions",
                "Safety planning",
                "Medication review",
                "Family involvement",
                "Crisis hotline information"
            ],
            "High": [
                "Immediate psychiatric evaluation",
                "24/7 monitoring or hospitalization",
                "Crisis intervention team activation",
                "Remove access to lethal means",
                "Family/caregiver notification"
            ],
            "Critical": [
                "🚨 IMMEDIATE EMERGENCY INTERVENTION",
                "Call 911 or emergency services",
                "24/7 monitoring required",
                "Psychiatric hospitalization",
                "Crisis team activation"
            ]
        }
        return recommendations.get(risk_level, ["Consult with mental health professional"])

def main():
    st.markdown('<h1 class="main-header">🧠 Mental Health Risk Assessment System</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem;">AI-powered predictive analytics for mental health crisis prevention</p>', unsafe_allow_html=True)
    
    # Initialize the risk assessment system
    risk_assessor = SimpleRiskAssessment()
    
    # Sidebar for patient information
    st.sidebar.header("Patient Information")
    
    # Demographics
    st.sidebar.subheader("Demographics")
    age = st.sidebar.slider("Age", 18, 85, 35)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Non-binary"])
    ethnicity = st.sidebar.selectbox("Ethnicity", 
        ["White", "Black", "Hispanic", "Asian", "Native American", "Other"])
    
    # Clinical Scores
    st.sidebar.subheader("Clinical Assessment")
    phq9_score = st.sidebar.slider("PHQ-9 Score (Depression)", 0, 27, 10)
    gad7_score = st.sidebar.slider("GAD-7 Score (Anxiety)", 0, 21, 8)
    hopelessness_score = st.sidebar.slider("Hopelessness Score", 0, 20, 6)
    cssrs_score = st.sidebar.slider("CSSRS Score (Suicide Risk)", 0, 25, 4)
    
    # Behavioral Indicators
    st.sidebar.subheader("Behavioral Indicators")
    social_isolation = st.sidebar.slider("Social Isolation (0-10)", 0, 10, 5)
    substance_use = st.sidebar.slider("Substance Use (0-10)", 0, 10, 3)
    life_events = st.sidebar.slider("Recent Life Events (0-8)", 0, 8, 2)
    
    # Treatment History
    st.sidebar.subheader("Treatment History")
    previous_attempts = st.sidebar.slider("Previous Suicide Attempts", 0, 5, 0)
    compliance = st.sidebar.slider("Treatment Compliance (%)", 0, 100, 75)
    family_suicide = st.sidebar.checkbox("Family History of Suicide")
    
    # Assessment button
    if st.sidebar.button("Assess Risk", type="primary"):
        # Create patient data
        patient_data = {
            'age': age,
            'gender': gender,
            'ethnicity': ethnicity,
            'phq9_score': phq9_score,
            'gad7_score': gad7_score,
            'hopelessness_score': hopelessness_score,
            'cssrs_score': cssrs_score,
            'social_isolation': social_isolation,
            'substance_use': substance_use,
            'recent_life_events': life_events,
            'previous_suicide_attempts': previous_attempts,
            'treatment_compliance': compliance,
            'family_suicide': int(family_suicide)
        }
        
        # Calculate risk
        risk_score = risk_assessor.calculate_risk_score(patient_data)
        risk_level = risk_assessor.determine_risk_level(risk_score)
        recommendations = risk_assessor.get_recommendations(risk_level)
        
        # Display results
        st.markdown('<h2>Risk Assessment Results</h2>', unsafe_allow_html=True)
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Risk Probability", f"{risk_score:.1%}")
        
        with col2:
            risk_class = f"risk-{risk_level.lower()}" if risk_level.lower() in ['high', 'moderate', 'low'] else "risk-high"
            st.markdown(f'<div class="metric-card"><h3>Risk Level</h3><p class="{risk_class}">{risk_level}</p></div>', 
                       unsafe_allow_html=True)
        
        with col3:
            if risk_level in ["High", "Critical"]:
                st.metric("Recommended Action", "Immediate Intervention")
            elif risk_level == "Moderate":
                st.metric("Recommended Action", "Close Monitoring")
            else:
                st.metric("Recommended Action", "Regular Check-ins")
        
        with col4:
            st.metric("Assessment Date", datetime.now().strftime('%Y-%m-%d'))
        
        # Patient Summary
        st.subheader("Patient Summary")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Demographics**")
            st.write(f"Age: {age}")
            st.write(f"Gender: {gender}")
            st.write(f"Ethnicity: {ethnicity}")
        
        with col2:
            st.markdown("**Clinical Scores**")
            st.write(f"PHQ-9 (Depression): {phq9_score}/27")
            st.write(f"GAD-7 (Anxiety): {gad7_score}/21")
            st.write(f"Hopelessness: {hopelessness_score}/20")
            st.write(f"CSSRS (Suicide Risk): {cssrs_score}/25")
        
        # Risk Factors Analysis
        st.subheader("Risk Factors Analysis")
        
        risk_factors = {
            'Depression (PHQ-9)': phq9_score / 27 * 0.20,
            'Anxiety (GAD-7)': gad7_score / 21 * 0.15,
            'Hopelessness': hopelessness_score / 20 * 0.25,
            'Suicide Risk (CSSRS)': cssrs_score / 25 * 0.30,
            'Previous Attempts': previous_attempts / 5 * 0.35,
            'Social Isolation': social_isolation / 10 * 0.10,
            'Substance Use': substance_use / 10 * 0.12,
            'Life Events': life_events / 8 * 0.08
        }
        
        # Create a simple bar chart using st.bar_chart
        risk_df = pd.DataFrame(list(risk_factors.items()), columns=['Risk Factor', 'Contribution'])
        st.bar_chart(risk_df.set_index('Risk Factor'))
        
        # Clinical Recommendations
        st.subheader("Clinical Recommendations")
        
        if risk_level in ["High", "Critical"]:
            st.error("🚨 **IMMEDIATE ACTION REQUIRED**")
        elif risk_level == "Moderate":
            st.warning("⚠️ **ENHANCED MONITORING**")
        else:
            st.success("✅ **STANDARD CARE**")
        
        for i, rec in enumerate(recommendations, 1):
            st.write(f"{i}. {rec}")
        
        # Export functionality
        st.subheader("Export Assessment")
        
        # Create comprehensive report data
        report_data = {
            'Assessment_Date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Risk_Probability': f"{risk_score:.3f}",
            'Risk_Level': risk_level,
            'Risk_Percentage': f"{risk_score*100:.1f}%",
            'Recommended_Action': "Immediate Intervention" if risk_level in ["High", "Critical"] else "Close Monitoring" if risk_level == "Moderate" else "Regular Check-ins",
            'Age': age,
            'Gender': gender,
            'Ethnicity': ethnicity,
            'PHQ9_Score': phq9_score,
            'GAD7_Score': gad7_score,
            'Hopelessness_Score': hopelessness_score,
            'CSSRS_Score': cssrs_score,
            'Social_Isolation': social_isolation,
            'Substance_Use': substance_use,
            'Recent_Life_Events': life_events,
            'Previous_Suicide_Attempts': previous_attempts,
            'Treatment_Compliance': f"{compliance}%",
            'Family_History_Suicide': "Yes" if family_suicide else "No"
        }
        
        # Add risk factor contributions
        risk_factors = {
            'Depression_Contribution': f"{phq9_score / 27 * 0.20:.3f}",
            'Anxiety_Contribution': f"{gad7_score / 21 * 0.15:.3f}",
            'Hopelessness_Contribution': f"{hopelessness_score / 20 * 0.25:.3f}",
            'Suicide_Risk_Contribution': f"{cssrs_score / 25 * 0.30:.3f}",
            'Previous_Attempts_Contribution': f"{previous_attempts / 5 * 0.35:.3f}",
            'Social_Isolation_Contribution': f"{social_isolation / 10 * 0.10:.3f}",
            'Substance_Use_Contribution': f"{substance_use / 10 * 0.12:.3f}",
            'Life_Events_Contribution': f"{life_events / 8 * 0.08:.3f}"
        }
        report_data.update(risk_factors)
        
        # Add clinical recommendations
        recommendations_text = "; ".join(recommendations)
        report_data['Clinical_Recommendations'] = recommendations_text
        
        # Create CSV download
        report_df = pd.DataFrame([report_data])
        csv_data = report_df.to_csv(index=False)
        
        # Create a more detailed text report
        text_report = f"""
MENTAL HEALTH RISK ASSESSMENT REPORT
====================================
Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

PATIENT INFORMATION:
- Age: {age}
- Gender: {gender}
- Ethnicity: {ethnicity}

CLINICAL ASSESSMENT:
- PHQ-9 Score (Depression): {phq9_score}/27
- GAD-7 Score (Anxiety): {gad7_score}/21
- Hopelessness Score: {hopelessness_score}/20
- CSSRS Score (Suicide Risk): {cssrs_score}/25

BEHAVIORAL INDICATORS:
- Social Isolation: {social_isolation}/10
- Substance Use: {substance_use}/10
- Recent Life Events: {life_events}/8

TREATMENT HISTORY:
- Previous Suicide Attempts: {previous_attempts}
- Treatment Compliance: {compliance}%
- Family History of Suicide: {"Yes" if family_suicide else "No"}

RISK ASSESSMENT RESULTS:
- Risk Probability: {risk_score:.3f} ({risk_score*100:.1f}%)
- Risk Level: {risk_level}
- Recommended Action: {"Immediate Intervention" if risk_level in ["High", "Critical"] else "Close Monitoring" if risk_level == "Moderate" else "Regular Check-ins"}

RISK FACTOR CONTRIBUTIONS:
- Depression (PHQ-9): {phq9_score / 27 * 0.20:.3f}
- Anxiety (GAD-7): {gad7_score / 21 * 0.15:.3f}
- Hopelessness: {hopelessness_score / 20 * 0.25:.3f}
- Suicide Risk (CSSRS): {cssrs_score / 25 * 0.30:.3f}
- Previous Attempts: {previous_attempts / 5 * 0.35:.3f}
- Social Isolation: {social_isolation / 10 * 0.10:.3f}
- Substance Use: {substance_use / 10 * 0.12:.3f}
- Life Events: {life_events / 8 * 0.08:.3f}

CLINICAL RECOMMENDATIONS:
{chr(10).join(f"{i+1}. {rec}" for i, rec in enumerate(recommendations))}

IMPORTANT NOTES:
- This assessment is for clinical reference only
- All decisions should be made by qualified mental health professionals
- For emergency situations, contact 911 or emergency services immediately
- This report should be kept confidential and secure

Generated by Mental Health Risk Assessment System
        """
        
        # Generate PDF report
        pdf_generator = MentalHealthPDFGenerator()
        pdf_buffer = pdf_generator.generate_pdf_report(
            patient_data, risk_score, risk_level, recommendations
        )
        
        # Provide three download options
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.download_button(
                label="📊 Download CSV Report",
                data=csv_data,
                file_name=f"mental_health_assessment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                help="Download detailed assessment data in CSV format"
            )
        
        with col2:
            st.download_button(
                label="📄 Download Text Report",
                data=text_report,
                file_name=f"mental_health_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                help="Download comprehensive assessment report in text format"
            )
        
        with col3:
            st.download_button(
                label="📋 Download PDF Report",
                data=pdf_buffer.getvalue(),
                file_name=f"mental_health_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf",
                help="Download professional PDF report with graphs and visualizations"
            )
        
        # Show preview of the report
        with st.expander("📋 Preview Report"):
            st.text(text_report)
        
        # Show PDF preview
        with st.expander("📋 PDF Report Preview"):
            st.markdown("**PDF Report includes:**")
            st.markdown("""
            - 🎯 **Risk Assessment Summary** with gauge chart
            - 👤 **Complete Patient Information** in organized tables
            - 📊 **Clinical Assessment Visualization** (radar chart)
            - 📈 **Risk Factor Analysis** with bar charts
            - 💡 **Clinical Recommendations** with action items
            - ⚠️ **Important Notes** and disclaimers
            """)
            st.success("✅ PDF report is ready for download with professional formatting and visualizations!")
    
    # Information section
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About This System")
    st.sidebar.markdown("""
    This AI-powered system helps mental health professionals:
    
    - **Predict crisis risk** using comprehensive patient data
    - **Enable early intervention** for high-risk patients
    - **Provide clinical recommendations** based on risk levels
    - **Track risk factors** and their contributions
    
    **Note**: This is a demonstration system and should not replace clinical judgment.
    """)
    
    # Show sample data if no assessment has been run
    if 'risk_score' not in locals():
        st.info("👈 Use the sidebar to enter patient information and click 'Assess Risk' to begin.")

if __name__ == "__main__":
    main() 