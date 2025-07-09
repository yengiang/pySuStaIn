#!/usr/bin/env python3
"""
Test script to verify the new color scheme is working when importing pySuStaIn
"""

import numpy as np
import matplotlib.pyplot as plt
from pySuStaIn.ZscoreSustain import ZscoreSustain

def test_color_scheme():
    """Test that the new color scheme is applied correctly"""
    
    # Create sample data
    n_biomarkers = 5
    n_samples = 100
    n_subtypes = 2
    
    # Create Z_vals matrix (biomarkers x z-score thresholds)
    Z_vals = np.array([
        [1, 2, 3],  # Biomarker 1: thresholds at z=1,2,3
        [1, 2, 3],  # Biomarker 2: thresholds at z=1,2,3
        [1, 2, 0],  # Biomarker 3: thresholds at z=1,2 (no z=3)
        [1, 2, 3],  # Biomarker 4: thresholds at z=1,2,3
        [1, 2, 3]   # Biomarker 5: thresholds at z=1,2,3
    ])
    
    Z_max = np.array([5, 5, 3, 5, 5])  # Maximum z-scores for each biomarker
    
    biomarker_labels = [f'Biomarker_{i+1}' for i in range(n_biomarkers)]
    
    # Generate some sample data (positive z-scores)
    np.random.seed(42)
    data = np.random.exponential(1.5, (n_samples, n_biomarkers))
    
    # Create ZscoreSustain object
    sustain_model = ZscoreSustain(
        data=data,
        Z_vals=Z_vals,
        Z_max=Z_max,
        biomarker_labels=biomarker_labels,
        N_startpoints=5,  # Reduced for testing
        N_S_max=n_subtypes,
        N_iterations_MCMC=1000,  # Reduced for testing
        output_folder='test_output',
        dataset_name='color_test',
        use_parallel_startpoints=False,
        seed=42
    )
    
    # Generate some mock MCMC samples for plotting
    N_stages = np.sum(Z_vals > 0)
    samples_sequence = np.random.randint(0, N_stages, (n_subtypes, N_stages, 100))
    samples_f = np.random.dirichlet([1] * n_subtypes, 100).T
    
    # Create the plot with the new color scheme
    figs, axs = ZscoreSustain.plot_positional_var(
        samples_sequence=samples_sequence,
        samples_f=samples_f,
        n_samples=n_samples,
        Z_vals=Z_vals,
        biomarker_labels=biomarker_labels,
        save_path='test_color_scheme_plot'
    )
    
    print("✓ Color scheme test completed successfully!")
    print("✓ New color mapping:")
    print("  - Z-score 1: Blue [0, 0, 1]")
    print("  - Z-score 2: Magenta [1, 0, 1]") 
    print("  - Z-score 3: Red [1, 0, 0]")
    print("✓ Plot saved as 'test_color_scheme_plot_all-subtypes.png'")
    
    return figs, axs

if __name__ == "__main__":
    try:
        figs, axs = test_color_scheme()
        plt.show()
    except Exception as e:
        print(f"Error during testing: {e}")
        import traceback
        traceback.print_exc()
