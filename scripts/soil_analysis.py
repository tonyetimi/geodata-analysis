#!/usr/bin/env python3
"""
Geological Soil Analysis Script
Basic analysis of soil composition data for energy and mining sectors
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class SoilAnalyzer:
    def __init__(self, data_file):
        """
        Initialize soil analyzer with data file
        """
        self.data = pd.read_csv(data_file)
        self.results = {}
    
    def analyze_composition(self):
        """Analyze soil composition percentages"""
        composition_cols = ['sand_percent', 'clay_percent', 'silt_percent']
        composition = self.data[composition_cols].mean()
        self.results['composition'] = composition
        return composition
    
    def calculate_bearing_capacity(self):
        """Estimate soil bearing capacity for construction"""
        # Simple estimation based on composition
        composition = self.analyze_composition()
        sand_ratio = composition['sand_percent'] / 100
        bearing_capacity = 100 + (sand_ratio * 200)  # kN/m² estimation
        self.results['bearing_capacity'] = bearing_capacity
        return bearing_capacity
    
    def plot_composition(self):
        """Create soil composition pie chart"""
        composition = self.analyze_composition()
        plt.figure(figsize=(10, 8))
        plt.pie(composition, labels=composition.index, autopct='%1.1f%%', startangle=90)
        plt.title('Soil Composition Analysis - Foundation Assessment')
        plt.savefig('soil_composition.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def generate_report(self):
        """Generate comprehensive analysis report"""
        composition = self.analyze_composition()
        bearing_capacity = self.calculate_bearing_capacity()
        
        report = f"""
        GEOTECHNICAL SOIL ANALYSIS REPORT
        =================================
        
        SAMPLES ANALYZED: {len(self.data)}
        
        AVERAGE COMPOSITION:
        - Sand:    {composition['sand_percent']:.1f}%
        - Clay:    {composition['clay_percent']:.1f}%
        - Silt:    {composition['silt_percent']:.1f}%
        
        ENGINEERING PROPERTIES:
        - Estimated Bearing Capacity: {bearing_capacity:.1f} kN/m²
        - Foundation Suitability:     {'GOOD' if bearing_capacity > 150 else 'MODERATE'}
        
        RECOMMENDATIONS:
        - Foundation type: {'Shallow' if bearing_capacity > 180 else 'Deep'}
        - Further testing: {'Not required' if bearing_capacity > 200 else 'Recommended'}
        """
        return report

# Example usage and test data
def create_sample_data():
    """Create sample soil data for demonstration"""
    sample_data = {
        'sample_id': range(1, 11),
        'sand_percent': [45, 52, 48, 60, 55, 42, 58, 50, 47, 53],
        'clay_percent': [25, 20, 22, 15, 18, 28, 17, 22, 25, 20],
        'silt_percent': [30, 28, 30, 25, 27, 30, 25, 28, 28, 27]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv('sample_soil_data.csv', index=False)
    return df

if __name__ == "__main__":
    # Create sample data
    create_sample_data()
    
    # Run analysis
    analyzer = SoilAnalyzer('sample_soil_data.csv')
    print(analyzer.generate_report())
    analyzer.plot_composition()
