import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from tqdm import tqdm

class MentalHealthDataGenerator:
    def __init__(self, seed=42):
        np.random.seed(seed)
        random.seed(seed)
        
    def generate_demographics(self, n_samples):
        """Generate demographic data"""
        ages = np.random.normal(35, 15, n_samples).astype(int)
        ages = np.clip(ages, 18, 85)
        
        genders = np.random.choice(['Male', 'Female', 'Non-binary'], n_samples, p=[0.45, 0.50, 0.05])
        
        ethnicities = np.random.choice([
            'White', 'Black', 'Hispanic', 'Asian', 'Native American', 'Other'
        ], n_samples, p=[0.60, 0.12, 0.18, 0.06, 0.02, 0.02])
        
        socioeconomic_status = np.random.choice([
            'Low', 'Lower-middle', 'Middle', 'Upper-middle', 'High'
        ], n_samples, p=[0.20, 0.25, 0.30, 0.20, 0.05])
        
        return pd.DataFrame({
            'age': ages,
            'gender': genders,
            'ethnicity': ethnicities,
            'socioeconomic_status': socioeconomic_status
        })
    
    def generate_family_history(self, n_samples):
        """Generate family history data"""
        family_depression = np.random.binomial(1, 0.35, n_samples)
        family_anxiety = np.random.binomial(1, 0.30, n_samples)
        family_suicide = np.random.binomial(1, 0.08, n_samples)
        family_substance_abuse = np.random.binomial(1, 0.25, n_samples)
        
        return pd.DataFrame({
            'family_depression': family_depression,
            'family_anxiety': family_anxiety,
            'family_suicide': family_suicide,
            'family_substance_abuse': family_substance_abuse
        })
    
    def generate_clinical_scores(self, n_samples):
        """Generate clinical assessment scores"""
        # PHQ-9 (Depression): 0-27, higher = worse
        phq9_scores = np.random.poisson(8, n_samples)
        phq9_scores = np.clip(phq9_scores, 0, 27)
        
        # GAD-7 (Anxiety): 0-21, higher = worse
        gad7_scores = np.random.poisson(6, n_samples)
        gad7_scores = np.clip(gad7_scores, 0, 21)
        
        # Beck Hopelessness Scale: 0-20, higher = worse
        hopelessness_scores = np.random.poisson(5, n_samples)
        hopelessness_scores = np.clip(hopelessness_scores, 0, 20)
        
        # Columbia Suicide Severity Rating Scale: 0-25, higher = worse
        cssrs_scores = np.random.poisson(3, n_samples)
        cssrs_scores = np.clip(cssrs_scores, 0, 25)
        
        return pd.DataFrame({
            'phq9_score': phq9_scores,
            'gad7_score': gad7_scores,
            'hopelessness_score': hopelessness_scores,
            'cssrs_score': cssrs_scores
        })
    
    def generate_behavioral_indicators(self, n_samples):
        """Generate behavioral and lifestyle indicators"""
        # Sleep patterns (hours per night)
        sleep_hours = np.random.normal(7.2, 1.5, n_samples)
        sleep_hours = np.clip(sleep_hours, 3, 12)
        
        # Social isolation (0-10 scale, higher = more isolated)
        social_isolation = np.random.poisson(4, n_samples)
        social_isolation = np.clip(social_isolation, 0, 10)
        
        # Recent life events (count of stressful events in last 6 months)
        life_events = np.random.poisson(2, n_samples)
        life_events = np.clip(life_events, 0, 8)
        
        # Substance use (0-10 scale, higher = more use)
        substance_use = np.random.poisson(2, n_samples)
        substance_use = np.clip(substance_use, 0, 10)
        
        # Risk-taking behaviors (0-10 scale)
        risk_taking = np.random.poisson(3, n_samples)
        risk_taking = np.clip(risk_taking, 0, 10)
        
        return pd.DataFrame({
            'sleep_hours': sleep_hours,
            'social_isolation': social_isolation,
            'recent_life_events': life_events,
            'substance_use': substance_use,
            'risk_taking_behaviors': risk_taking
        })
    
    def generate_treatment_history(self, n_samples):
        """Generate treatment history data"""
        # Previous suicide attempts
        previous_attempts = np.random.poisson(0.3, n_samples)
        previous_attempts = np.clip(previous_attempts, 0, 5)
        
        # Hospitalizations
        hospitalizations = np.random.poisson(0.5, n_samples)
        hospitalizations = np.clip(hospitalizations, 0, 8)
        
        # Current medications (count)
        current_medications = np.random.poisson(1.5, n_samples)
        current_medications = np.clip(current_medications, 0, 6)
        
        # Treatment compliance (0-100%)
        treatment_compliance = np.random.normal(75, 20, n_samples)
        treatment_compliance = np.clip(treatment_compliance, 0, 100)
        
        # Days since last therapy session
        days_since_therapy = np.random.exponential(30, n_samples)
        days_since_therapy = np.clip(days_since_therapy, 0, 365)
        
        return pd.DataFrame({
            'previous_suicide_attempts': previous_attempts,
            'hospitalizations': hospitalizations,
            'current_medications': current_medications,
            'treatment_compliance': treatment_compliance,
            'days_since_therapy': days_since_therapy
        })
    
    def generate_environmental_factors(self, n_samples):
        """Generate environmental and contextual factors"""
        # Housing stability (0-10 scale, higher = more stable)
        housing_stability = np.random.normal(7, 2, n_samples)
        housing_stability = np.clip(housing_stability, 0, 10)
        
        # Employment status
        employment_status = np.random.choice([
            'Employed', 'Unemployed', 'Part-time', 'Student', 'Retired', 'Disabled'
        ], n_samples, p=[0.60, 0.15, 0.10, 0.08, 0.05, 0.02])
        
        # Access to healthcare (0-10 scale)
        healthcare_access = np.random.normal(7, 2, n_samples)
        healthcare_access = np.clip(healthcare_access, 0, 10)
        
        # Social support (0-10 scale, higher = more support)
        social_support = np.random.normal(6, 2, n_samples)
        social_support = np.clip(social_support, 0, 10)
        
        return pd.DataFrame({
            'housing_stability': housing_stability,
            'employment_status': employment_status,
            'healthcare_access': healthcare_access,
            'social_support': social_support
        })
    
    def generate_risk_outcomes(self, features_df, n_samples):
        """Generate risk outcomes based on features"""
        # Create risk score based on features with more realistic weighting
        risk_score = (
            features_df['phq9_score'] * 0.20 +
            features_df['gad7_score'] * 0.15 +
            features_df['hopelessness_score'] * 0.25 +
            features_df['cssrs_score'] * 0.30 +
            features_df['previous_suicide_attempts'] * 0.35 +
            features_df['social_isolation'] * 0.10 +
            features_df['substance_use'] * 0.12 +
            features_df['recent_life_events'] * 0.08 +
            (10 - features_df['social_support']) * 0.08 +
            (10 - features_df['treatment_compliance']) * 0.05 +
            features_df['family_suicide'] * 0.20 +
            features_df['family_depression'] * 0.05 +
            features_df['family_anxiety'] * 0.05 +
            features_df['family_substance_abuse'] * 0.08
        )
        
        # Add some randomness and ensure wider distribution
        risk_score += np.random.normal(0, 5, n_samples)
        risk_score = np.clip(risk_score, 0, 100)
        
        # Determine risk level with more realistic thresholds
        risk_levels = []
        for score in risk_score:
            if score < 15:
                risk_levels.append('Low')
            elif score < 35:
                risk_levels.append('Moderate')
            elif score < 55:
                risk_levels.append('High')
            else:
                risk_levels.append('Critical')
        
        # Generate actual crisis events with higher base probability
        crisis_probability = np.maximum(risk_score / 100 * 0.15, 0.001)  # Minimum 0.1% probability
        crisis_events = np.random.binomial(1, crisis_probability, n_samples)
        
        # Generate time to crisis (in days, 0-365)
        time_to_crisis = np.random.exponential(180, n_samples)
        time_to_crisis = np.clip(time_to_crisis, 0, 365)
        
        # Only assign crisis time to those who actually have events
        time_to_crisis = np.where(crisis_events == 1, time_to_crisis, np.nan)
        
        return pd.DataFrame({
            'risk_score': risk_score,
            'risk_level': risk_levels,
            'crisis_event': crisis_events,
            'time_to_crisis_days': time_to_crisis
        })
    
    def generate_dataset(self, n_samples=10000):
        """Generate complete dataset"""
        print(f"Generating {n_samples} patient records...")
        
        # Generate all feature categories
        demographics = self.generate_demographics(n_samples)
        family_history = self.generate_family_history(n_samples)
        clinical_scores = self.generate_clinical_scores(n_samples)
        behavioral = self.generate_behavioral_indicators(n_samples)
        treatment_history = self.generate_treatment_history(n_samples)
        environmental = self.generate_environmental_factors(n_samples)
        
        # Combine all features
        features_df = pd.concat([
            demographics, family_history, clinical_scores, 
            behavioral, treatment_history, environmental
        ], axis=1)
        
        # Generate outcomes
        outcomes = self.generate_risk_outcomes(features_df, n_samples)
        
        # Combine features and outcomes
        final_df = pd.concat([features_df, outcomes], axis=1)
        
        # Add patient ID
        final_df.insert(0, 'patient_id', range(1, n_samples + 1))
        
        # Add timestamp
        final_df['assessment_date'] = datetime.now().strftime('%Y-%m-%d')
        
        return final_df
    
    def save_dataset(self, df, filename='mental_health_dataset.csv'):
        """Save dataset to CSV"""
        df.to_csv(filename, index=False)
        print(f"Dataset saved to {filename}")
        print(f"Shape: {df.shape}")
        print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

if __name__ == "__main__":
    # Generate dataset
    generator = MentalHealthDataGenerator(seed=42)
    dataset = generator.generate_dataset(n_samples=50000)  # 50k records
    
    # Save dataset
    generator.save_dataset(dataset, 'mental_health_dataset.csv')
    
    # Print summary statistics
    print("\nDataset Summary:")
    print(f"Total patients: {len(dataset)}")
    print(f"Crisis events: {dataset['crisis_event'].sum()} ({dataset['crisis_event'].mean()*100:.2f}%)")
    print(f"Risk level distribution:")
    print(dataset['risk_level'].value_counts()) 