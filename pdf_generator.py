import io
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import numpy as np
from datetime import datetime

class MentalHealthPDFGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
    
    def setup_custom_styles(self):
        """Setup custom paragraph styles for the report"""
        # Title style
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor('#1f77b4')
        )
        
        # Section header style
        self.section_style = ParagraphStyle(
            'CustomSection',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=colors.HexColor('#2c3e50')
        )
        
        # Normal text style
        self.normal_style = ParagraphStyle(
            'CustomNormal',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=6
        )
        
        # Risk level style
        self.risk_style = ParagraphStyle(
            'RiskLevel',
            parent=self.styles['Normal'],
            fontSize=14,
            spaceAfter=6,
            alignment=TA_CENTER,
            textColor=colors.white,
            backColor=colors.HexColor('#e74c3c')
        )
    
    def create_risk_gauge_chart(self, risk_score, risk_level):
        """Create a risk gauge chart"""
        fig, ax = plt.subplots(figsize=(8, 4))
        
        # Create gauge
        theta = np.linspace(0, np.pi, 100)
        radius = 1
        
        # Color mapping for risk levels
        color_map = {
            'Low': '#2ecc71',
            'Moderate': '#f39c12', 
            'High': '#e67e22',
            'Critical': '#e74c3c'
        }
        
        # Create the gauge arc
        ax.plot(radius * np.cos(theta), radius * np.sin(theta), 'k-', linewidth=3)
        
        # Fill the gauge based on risk level
        risk_angle = risk_score * np.pi
        theta_fill = np.linspace(0, risk_angle, 50)
        ax.fill_between(radius * np.cos(theta_fill), 0, radius * np.sin(theta_fill), 
                       color=color_map.get(risk_level, '#e74c3c'), alpha=0.7)
        
        # Add risk level text
        ax.text(0, -0.3, risk_level, ha='center', va='center', fontsize=16, fontweight='bold',
               color=color_map.get(risk_level, '#e74c3c'))
        
        # Add percentage
        ax.text(0, -0.6, f'{risk_score*100:.1f}%', ha='center', va='center', fontsize=14)
        
        # Add labels
        ax.text(-0.9, 0.1, 'Low', ha='center', va='center', fontsize=10)
        ax.text(0.9, 0.1, 'Critical', ha='center', va='center', fontsize=10)
        
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-0.8, 1.2)
        ax.axis('off')
        ax.set_aspect('equal')
        
        # Save to buffer
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        img_buffer.seek(0)
        plt.close()
        
        return img_buffer
    
    def create_risk_factors_chart(self, risk_factors):
        """Create a bar chart of risk factors"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        factors = list(risk_factors.keys())
        values = list(risk_factors.values())
        
        # Create horizontal bar chart
        bars = ax.barh(factors, values, color='#3498db', alpha=0.7)
        
        # Add value labels on bars
        for i, (bar, value) in enumerate(zip(bars, values)):
            ax.text(value + 0.001, bar.get_y() + bar.get_height()/2, 
                   f'{value:.3f}', va='center', fontsize=10)
        
        ax.set_xlabel('Contribution to Risk Score', fontsize=12)
        ax.set_title('Risk Factor Contributions', fontsize=14, fontweight='bold')
        ax.grid(axis='x', alpha=0.3)
        
        # Save to buffer
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        img_buffer.seek(0)
        plt.close()
        
        return img_buffer
    
    def create_clinical_scores_chart(self, clinical_scores):
        """Create a radar chart for clinical scores"""
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
        
        categories = list(clinical_scores.keys())
        values = list(clinical_scores.values())
        
        # Close the plot by appending first value
        values += values[:1]
        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
        angles += angles[:1]
        
        ax.plot(angles, values, 'o-', linewidth=2, color='#e74c3c')
        ax.fill(angles, values, alpha=0.25, color='#e74c3c')
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        ax.set_ylim(0, max(values) * 1.1)
        ax.set_title('Clinical Assessment Scores', fontsize=14, fontweight='bold', pad=20)
        
        # Save to buffer
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        img_buffer.seek(0)
        plt.close()
        
        return img_buffer
    
    def get_risk_color(self, risk_level):
        """Get color for risk level"""
        color_map = {
            'Low': '#2ecc71',
            'Moderate': '#f39c12',
            'High': '#e67e22', 
            'Critical': '#e74c3c'
        }
        return color_map.get(risk_level, '#e74c3c')
    
    def generate_pdf_report(self, patient_data, risk_score, risk_level, recommendations):
        """Generate comprehensive PDF report"""
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, 
                              topMargin=72, bottomMargin=72)
        
        story = []
        
        # Title
        story.append(Paragraph("MENTAL HEALTH RISK ASSESSMENT REPORT", self.title_style))
        story.append(Spacer(1, 20))
        
        # Assessment date
        story.append(Paragraph(f"Assessment Date: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", 
                              self.normal_style))
        story.append(Spacer(1, 20))
        
        # Risk Summary Section
        story.append(Paragraph("RISK ASSESSMENT SUMMARY", self.section_style))
        
        # Risk gauge chart
        gauge_img = self.create_risk_gauge_chart(risk_score, risk_level)
        story.append(Image(gauge_img, width=6*inch, height=3*inch))
        story.append(Spacer(1, 10))
        
        # Risk summary table
        risk_data = [
            ['Risk Probability', f'{risk_score:.3f} ({risk_score*100:.1f}%)'],
            ['Risk Level', risk_level],
            ['Recommended Action', self.get_recommended_action(risk_level)]
        ]
        
        risk_table = Table(risk_data, colWidths=[2*inch, 3*inch])
        risk_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ecf0f1')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ]))
        story.append(risk_table)
        story.append(Spacer(1, 20))
        
        # Patient Information Section
        story.append(Paragraph("PATIENT INFORMATION", self.section_style))
        
        patient_info = [
            ['Demographics', ''],
            ['Age', str(patient_data['age'])],
            ['Gender', patient_data['gender']],
            ['Ethnicity', patient_data['ethnicity']],
            ['', ''],
            ['Clinical Assessment', ''],
            ['PHQ-9 Score (Depression)', f"{patient_data['phq9_score']}/27"],
            ['GAD-7 Score (Anxiety)', f"{patient_data['gad7_score']}/21"],
            ['Hopelessness Score', f"{patient_data['hopelessness_score']}/20"],
            ['CSSRS Score (Suicide Risk)', f"{patient_data['cssrs_score']}/25"],
            ['', ''],
            ['Behavioral Indicators', ''],
            ['Social Isolation', f"{patient_data['social_isolation']}/10"],
            ['Substance Use', f"{patient_data['substance_use']}/10"],
            ['Recent Life Events', f"{patient_data['recent_life_events']}/8"],
            ['', ''],
            ['Treatment History', ''],
            ['Previous Suicide Attempts', str(patient_data['previous_suicide_attempts'])],
            ['Treatment Compliance', f"{patient_data['treatment_compliance']}%"],
            ['Family History of Suicide', "Yes" if patient_data['family_suicide'] else "No"]
        ]
        
        patient_table = Table(patient_info, colWidths=[2.5*inch, 2.5*inch])
        patient_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ecf0f1')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#34495e')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ]))
        story.append(patient_table)
        story.append(Spacer(1, 20))
        
        # Clinical Scores Chart
        story.append(Paragraph("CLINICAL ASSESSMENT VISUALIZATION", self.section_style))
        
        clinical_scores = {
            'PHQ-9\n(Depression)': patient_data['phq9_score'] / 27 * 100,
            'GAD-7\n(Anxiety)': patient_data['gad7_score'] / 21 * 100,
            'Hopelessness': patient_data['hopelessness_score'] / 20 * 100,
            'CSSRS\n(Suicide Risk)': patient_data['cssrs_score'] / 25 * 100
        }
        
        radar_img = self.create_clinical_scores_chart(clinical_scores)
        story.append(Image(radar_img, width=6*inch, height=6*inch))
        story.append(Spacer(1, 20))
        
        # Risk Factors Analysis
        story.append(Paragraph("RISK FACTOR ANALYSIS", self.section_style))
        
        risk_factors = {
            'Depression (PHQ-9)': patient_data['phq9_score'] / 27 * 0.20,
            'Anxiety (GAD-7)': patient_data['gad7_score'] / 21 * 0.15,
            'Hopelessness': patient_data['hopelessness_score'] / 20 * 0.25,
            'Suicide Risk (CSSRS)': patient_data['cssrs_score'] / 25 * 0.30,
            'Previous Attempts': patient_data['previous_suicide_attempts'] / 5 * 0.35,
            'Social Isolation': patient_data['social_isolation'] / 10 * 0.10,
            'Substance Use': patient_data['substance_use'] / 10 * 0.12,
            'Life Events': patient_data['recent_life_events'] / 8 * 0.08
        }
        
        factors_img = self.create_risk_factors_chart(risk_factors)
        story.append(Image(factors_img, width=6*inch, height=4*inch))
        story.append(Spacer(1, 20))
        
        # Clinical Recommendations
        story.append(Paragraph("CLINICAL RECOMMENDATIONS", self.section_style))
        
        for i, rec in enumerate(recommendations, 1):
            story.append(Paragraph(f"{i}. {rec}", self.normal_style))
        
        story.append(Spacer(1, 20))
        
        # Important Notes
        story.append(Paragraph("IMPORTANT NOTES", self.section_style))
        
        notes = [
            "• This assessment is for clinical reference only and should not replace professional judgment",
            "• All treatment decisions should be made by qualified mental health professionals",
            "• For emergency situations, contact 911 or emergency services immediately",
            "• This report should be kept confidential and secure in accordance with HIPAA guidelines",
            "• Regular reassessment is recommended to monitor risk level changes"
        ]
        
        for note in notes:
            story.append(Paragraph(note, self.normal_style))
        
        story.append(Spacer(1, 20))
        
        # Footer
        story.append(Paragraph("Generated by Mental Health Risk Assessment System", 
                              ParagraphStyle('Footer', parent=self.styles['Normal'], 
                                           fontSize=9, alignment=TA_CENTER, 
                                           textColor=colors.grey)))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer
    
    def get_recommended_action(self, risk_level):
        """Get recommended action based on risk level"""
        actions = {
            'Low': 'Regular Check-ins and Standard Care',
            'Moderate': 'Enhanced Monitoring and Safety Planning',
            'High': 'Immediate Psychiatric Evaluation and Crisis Intervention',
            'Critical': 'Emergency Intervention and 24/7 Monitoring'
        }
        return actions.get(risk_level, 'Consult with mental health professional')

if __name__ == "__main__":
    # Test the PDF generator
    generator = MentalHealthPDFGenerator()
    
    # Sample data
    patient_data = {
        'age': 35,
        'gender': 'Female',
        'ethnicity': 'White',
        'phq9_score': 15,
        'gad7_score': 12,
        'hopelessness_score': 8,
        'cssrs_score': 6,
        'social_isolation': 6,
        'substance_use': 4,
        'recent_life_events': 3,
        'previous_suicide_attempts': 1,
        'treatment_compliance': 70,
        'family_suicide': 0
    }
    
    risk_score = 0.45
    risk_level = 'High'
    recommendations = [
        'Immediate psychiatric evaluation',
        '24/7 monitoring or hospitalization',
        'Crisis intervention team activation',
        'Remove access to lethal means',
        'Family/caregiver notification'
    ]
    
    pdf_buffer = generator.generate_pdf_report(patient_data, risk_score, risk_level, recommendations)
    
    # Save test PDF
    with open('test_report.pdf', 'wb') as f:
        f.write(pdf_buffer.getvalue())
    
    print("Test PDF generated successfully!") 