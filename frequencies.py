"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if str(item) not in frequencies.keys():
            frequencies.update({str(item): 1})
        else:
            frequencies[str(item)] += 1
    return frequencies
