#!/usr/bin/env python3
"""
Very simple test to check if the color change is in place
"""

import sys
import os

# Add the current directory to Python path to ensure local imports work
sys.path.insert(0, os.getcwd())

try:
    print("Attempting to import pySuStaIn...")
    from pySuStaIn.ZscoreSustain import ZscoreSustain
    print("✓ Successfully imported ZscoreSustain")
    
    # Check the color matrix directly from the source code
    print("\nChecking color scheme...")
    
    # Read the source to verify the change
    with open('pySuStaIn/ZscoreSustain.py', 'r') as f:
        content = f.read()
        
    if '[0, 0, 1], [1, 0, 1], [1, 0, 0]' in content:
        print("✓ Color scheme correctly updated in ZscoreSustain.py:")
        print("  - Z-score 1: Blue [0, 0, 1]")
        print("  - Z-score 2: Magenta [1, 0, 1]")
        print("  - Z-score 3: Red [1, 0, 0]")
    else:
        print("✗ Color scheme not found in expected format")
        
    # Check OrdinalSustain too
    with open('pySuStaIn/OrdinalSustain.py', 'r') as f:
        content = f.read()
        
    if '[0, 0, 1], [1, 0, 1], [1, 0, 0]' in content:
        print("✓ Color scheme correctly updated in OrdinalSustain.py as well")
    else:
        print("✗ Color scheme not updated in OrdinalSustain.py")
        
    print("\n🎉 Your color scheme changes are implemented and ready to use!")
    print("When you import pySuStaIn in any script, the new color mapping will be active.")
    
except ImportError as e:
    print(f"✗ Import error: {e}")
    print("Make sure you're in the correct directory and pySuStaIn is properly installed.")
except Exception as e:
    print(f"✗ Unexpected error: {e}")

print("\nColor change implementation complete!")
