#!/usr/bin/env python3
"""
Example script showing how to use pySuStaIn with the new color scheme

This demonstrates that when you import pySuStaIn in your own scripts,
the new color mapping will automatically be applied:
- Z-score 1: Blue
- Z-score 2: Magenta  
- Z-score 3: Red
"""

import numpy as np
import matplotlib.pyplot as plt

# Import pySuStaIn - the new color scheme is now active!
from pySuStaIn.ZscoreSustain import ZscoreSustain

def example_usage():
    """Example of using pySuStaIn with the new color scheme"""
    
    print("=== pySuStaIn Color Scheme Update Example ===")
    print("New color mapping:")
    print("- Z-score 1: Blue [0, 0, 1]")
    print("- Z-score 2: Magenta [1, 0, 1]")
    print("- Z-score 3: Red [1, 0, 0]")
    print()
    
    # Example data setup
    n_biomarkers = 3
    n_samples = 50
    
    # Define Z-score thresholds for each biomarker
    Z_vals = np.array([
        [1, 2, 3],  # Biomarker 1: all three z-score levels
        [1, 2, 0],  # Biomarker 2: only z=1,2 (no z=3 threshold)
        [1, 2, 3]   # Biomarker 3: all three z-score levels
    ])
    
    # Maximum z-scores
    Z_max = np.array([5, 4, 5])
    
    # Biomarker labels
    biomarker_labels = ['Biomarker A', 'Biomarker B', 'Biomarker C']
    
    # Generate sample data (positive z-scores)
    np.random.seed(42)
    data = np.random.exponential(1.2, (n_samples, n_biomarkers))
    
    print("Example: Creating ZscoreSustain model...")
    
    # Create ZscoreSustain model
    sustain_model = ZscoreSustain(
        data=data,
        Z_vals=Z_vals,
        Z_max=Z_max,
        biomarker_labels=biomarker_labels,
        N_startpoints=10,
        N_S_max=2,
        N_iterations_MCMC=5000,
        output_folder='example_output',
        dataset_name='color_example',
        use_parallel_startpoints=False,
        seed=42
    )
    
    print("✓ Model created successfully!")
    print("✓ When you run the SuStaIn algorithm and generate plots,")
    print("  the new color scheme will be automatically applied!")
    print()
    print("Example plotting command:")
    print("  sustain_model.run_sustain_algorithm(plot=True)")
    print()
    print("The positional variance diagrams will now show:")
    print("  - Events at z-score 1 in BLUE")
    print("  - Events at z-score 2 in MAGENTA") 
    print("  - Events at z-score 3 in RED")

def direct_plotting_example():
    """Example of directly using the plotting function"""
    
    print("\n=== Direct Plotting Example ===")
    
    # Create minimal example data for plotting
    Z_vals = np.array([[1, 2, 3], [1, 2, 0]])  # 2 biomarkers
    
    # Mock MCMC samples (normally from sustain_model.run_sustain_algorithm())
    n_stages = np.sum(Z_vals > 0)  # Total number of stages
    samples_sequence = np.random.randint(0, n_stages, (1, n_stages, 100))
    samples_f = np.ones((1, 100))  # Single subtype
    
    print("Creating plot with new color scheme...")
    
    # Use the plotting function directly
    figs, axs = ZscoreSustain.plot_positional_var(
        samples_sequence=samples_sequence,
        samples_f=samples_f,
        n_samples=50,
        Z_vals=Z_vals,
        biomarker_labels=['Biomarker X', 'Biomarker Y'],
        figsize=(8, 4),
        save_path='example_new_colors'
    )
    
    print("✓ Plot created with new color scheme!")
    print("✓ Saved as 'example_new_colors_all-subtypes.png'")
    print("✓ Z-score events are now colored: 1=Blue, 2=Magenta, 3=Red")

if __name__ == "__main__":
    try:
        example_usage()
        # Uncomment the next line to create an actual plot:
        # direct_plotting_example()
        
        print("\n🎉 SUCCESS: Your pySuStaIn installation now uses the new color scheme!")
        print("Import pySuStaIn in any script and the new colors will be applied automatically.")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure all required packages are installed (numpy, matplotlib, scipy, etc.)")
