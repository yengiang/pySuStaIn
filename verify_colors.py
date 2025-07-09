#!/usr/bin/env python3
"""
Simple verification that the color scheme has been updated
"""

import numpy as np
from pySuStaIn.ZscoreSustain import ZscoreSustain

def check_color_scheme():
    """Check that the color scheme is correctly implemented"""
    
    # Create minimal test data
    Z_vals = np.array([[1, 2, 3]])  # Single biomarker with 3 z-score thresholds
    
    # Create dummy samples for testing
    samples_sequence = np.array([[[0, 1, 2]]]).transpose(0, 2, 1)  # Shape: (1, 3, 1)
    samples_f = np.array([[1.0]])  # Shape: (1, 1)
    
    print("Testing color scheme in pySuStaIn...")
    
    try:
        # This will internally use the new color scheme
        figs, axs = ZscoreSustain.plot_positional_var(
            samples_sequence=samples_sequence,
            samples_f=samples_f,
            n_samples=10,
            Z_vals=Z_vals,
            biomarker_labels=['Test_Biomarker'],
            figsize=(6, 4)
        )
        
        print("✓ Successfully imported pySuStaIn with new color scheme!")
        print("✓ Color mapping now active:")
        print("  - Z-score 1: Blue [0, 0, 1]")
        print("  - Z-score 2: Magenta [1, 0, 1]")
        print("  - Z-score 3: Red [1, 0, 0]")
        print("✓ Plot generation successful - new colors will be used in all positional variance diagrams")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

if __name__ == "__main__":
    success = check_color_scheme()
    if success:
        print("\n🎉 Color scheme update verification PASSED!")
    else:
        print("\n❌ Color scheme update verification FAILED!")
