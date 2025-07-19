import pandas as pd
import numpy as np
import json
from datetime import datetime

class SimpleMentalHealthDemo:
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
        
        # Add weighted contributions from each factor
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
                    normalized_value = (100 - patient_data[factor]) / 100  # Inverted
                else:
                    normalized_value = min(patient_data[factor] / 5, 1)  # Cap at 1
                
                risk_score += normalized_value * weight
        
        # Add some randomness for realism
        risk_score += np.random.normal(0, 0.05)
        risk_score = max(0, min(1, risk_score))  # Clamp between 0 and 1
        
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
    
    def assess_patient(self, patient_data):
        """Complete patient risk assessment"""
        print("=== MENTAL HEALTH RISK ASSESSMENT ===")
        print(f"Assessment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Calculate risk
        risk_score = self.calculate_risk_score(patient_data)
        risk_level = self.determine_risk_level(risk_score)
        
        # Display results
        print("PATIENT INFORMATION:")
        for key, value in patient_data.items():
            if key != 'patient_id':
                print(f"  {key.replace('_', ' ').title()}: {value}")
        print()
        
        print("RISK ASSESSMENT RESULTS:")
        print(f"  Risk Score: {risk_score:.3f} ({risk_score*100:.1f}%)")
        print(f"  Risk Level: {risk_level}")
        print()
        
        print("CLINICAL RECOMMENDATIONS:")
        recommendations = self.get_recommendations(risk_level)
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")
        print()
        
        # Risk factors analysis
        print("RISK FACTOR ANALYSIS:")
        for factor, weight in self.risk_weights.items():
            if factor in patient_data:
                if factor == 'phq9_score':
                    contribution = (patient_data[factor] / 27) * weight
                elif factor == 'gad7_score':
                    contribution = (patient_data[factor] / 21) * weight
                elif factor == 'hopelessness_score':
                    contribution = (patient_data[factor] / 20) * weight
                elif factor == 'cssrs_score':
                    contribution = (patient_data[factor] / 25) * weight
                elif factor == 'social_isolation':
                    contribution = (patient_data[factor] / 10) * weight
                elif factor == 'substance_use':
                    contribution = (patient_data[factor] / 10) * weight
                elif factor == 'recent_life_events':
                    contribution = (patient_data[factor] / 8) * weight
                elif factor == 'treatment_compliance':
                    contribution = ((100 - patient_data[factor]) / 100) * weight
                else:
                    contribution = min(patient_data[factor] / 5, 1) * weight
                
                print(f"  {factor.replace('_', ' ').title()}: {contribution:.3f}")
        
        return {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'recommendations': recommendations
        }
    
    def demo_multiple_patients(self):
        """Demonstrate with multiple patient scenarios"""
        print("=== DEMONSTRATION: MULTIPLE PATIENT SCENARIOS ===\n")
        
        # Sample patients with different risk profiles
        patients = [
            {
                'name': 'Patient A - Low Risk',
                'age': 25,
                'phq9_score': 5,
                'gad7_score': 4,
                'hopelessness_score': 2,
                'cssrs_score': 1,
                'previous_suicide_attempts': 0,
                'social_isolation': 3,
                'substance_use': 1,
                'recent_life_events': 1,
                'treatment_compliance': 90,
                'family_suicide': 0
            },
            {
                'name': 'Patient B - Moderate Risk',
                'age': 35,
                'phq9_score': 12,
                'gad7_score': 10,
                'hopelessness_score': 8,
                'cssrs_score': 6,
                'previous_suicide_attempts': 0,
                'social_isolation': 6,
                'substance_use': 4,
                'recent_life_events': 3,
                'treatment_compliance': 70,
                'family_suicide': 0
            },
            {
                'name': 'Patient C - High Risk',
                'age': 42,
                'phq9_score': 18,
                'gad7_score': 15,
                'hopelessness_score': 12,
                'cssrs_score': 10,
                'previous_suicide_attempts': 1,
                'social_isolation': 8,
                'substance_use': 7,
                'recent_life_events': 5,
                'treatment_compliance': 50,
                'family_suicide': 1
            },
            {
                'name': 'Patient D - Critical Risk',
                'age': 28,
                'phq9_score': 25,
                'gad7_score': 18,
                'hopelessness_score': 18,
                'cssrs_score': 20,
                'previous_suicide_attempts': 2,
                'social_isolation': 10,
                'substance_use': 9,
                'recent_life_events': 7,
                'treatment_compliance': 30,
                'family_suicide': 1
            }
        ]
        
        results = []
        for patient in patients:
            print(f"\n{'='*60}")
            print(f"ASSESSING: {patient['name']}")
            print(f"{'='*60}")
            
            result = self.assess_patient(patient)
            results.append({
                'patient': patient['name'],
                'risk_score': result['risk_score'],
                'risk_level': result['risk_level']
            })
            
            print(f"{'='*60}\n")
        
        # Summary
        print("SUMMARY OF ALL ASSESSMENTS:")
        print("-" * 50)
        for result in results:
            print(f"{result['patient']}: {result['risk_level']} Risk ({result['risk_score']*100:.1f}%)")
        
        return results

def main():
    """Main function to run the demonstration"""
    demo = SimpleMentalHealthDemo()
    
    print("🧠 MENTAL HEALTH RISK ASSESSMENT SYSTEM")
    print("AI-powered predictive analytics for crisis prevention")
    print("=" * 60)
    
    # Run demonstration with multiple patients
    results = demo.demo_multiple_patients()
    
    # Interactive assessment
    print("\n" + "=" * 60)
    print("INTERACTIVE ASSESSMENT")
    print("=" * 60)
    
    print("\nEnter patient information for a custom assessment:")
    
    try:
        age = int(input("Age: ") or "35")
        phq9 = int(input("PHQ-9 Score (0-27): ") or "10")
        gad7 = int(input("GAD-7 Score (0-21): ") or "8")
        hopelessness = int(input("Hopelessness Score (0-20): ") or "6")
        cssrs = int(input("CSSRS Score (0-25): ") or "4")
        previous_attempts = int(input("Previous Suicide Attempts: ") or "0")
        social_isolation = int(input("Social Isolation (0-10): ") or "5")
        substance_use = int(input("Substance Use (0-10): ") or "3")
        life_events = int(input("Recent Life Events (0-8): ") or "2")
        compliance = int(input("Treatment Compliance % (0-100): ") or "75")
        family_suicide = int(input("Family History of Suicide (0/1): ") or "0")
        
        custom_patient = {
            'age': age,
            'phq9_score': phq9,
            'gad7_score': gad7,
            'hopelessness_score': hopelessness,
            'cssrs_score': cssrs,
            'previous_suicide_attempts': previous_attempts,
            'social_isolation': social_isolation,
            'substance_use': substance_use,
            'recent_life_events': life_events,
            'treatment_compliance': compliance,
            'family_suicide': family_suicide
        }
        
        print("\n" + "=" * 60)
        demo.assess_patient(custom_patient)
        
    except ValueError:
        print("Invalid input. Using default values for demonstration.")
        
        default_patient = {
            'age': 35,
            'phq9_score': 10,
            'gad7_score': 8,
            'hopelessness_score': 6,
            'cssrs_score': 4,
            'previous_suicide_attempts': 0,
            'social_isolation': 5,
            'substance_use': 3,
            'recent_life_events': 2,
            'treatment_compliance': 75,
            'family_suicide': 0
        }
        
        demo.assess_patient(default_patient)
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nThis system demonstrates how AI can assist mental health professionals")
    print("in identifying patients at risk of crisis and providing appropriate")
    print("clinical recommendations for intervention and treatment.")

if __name__ == "__main__":
    main() 