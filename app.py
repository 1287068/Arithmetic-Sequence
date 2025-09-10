import streamlit as st

def generate_arithmetic_sequence(first_term, common_diff, num_terms):
    """
    Generate an arithmetic sequence given the first term, common difference, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_diff (float): The common difference between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: The arithmetic sequence as a list of numbers
    """
    if num_terms <= 0:
        return []
    
    sequence = []
    for i in range(num_terms):
        term = first_term + (i * common_diff)
        sequence.append(term)
    
    return sequence

def generate_geometric_sequence(first_term, common_ratio, num_terms):
    """
    Generate a geometric sequence given the first term, common ratio, and number of terms.
    
    Args:
        first_term (float): The first term of the sequence
        common_ratio (float): The common ratio between consecutive terms
        num_terms (int): The number of terms to generate
    
    Returns:
        list: The geometric sequence as a list of numbers
    """
    if num_terms <= 0:
        return []
    
    sequence = []
    for i in range(num_terms):
        term = first_term * (common_ratio ** i)
        sequence.append(term)
    
    return sequence

def main():
    # Set page title and header
    st.set_page_config(
        page_title="Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    st.title("🔢 Sequence Generator")
    st.markdown("Generate arithmetic or geometric sequences with detailed calculations and formulas.")
    
    # Sequence type selector
    sequence_type = st.selectbox(
        "Select Sequence Type",
        ["Arithmetic", "Geometric"],
        help="Choose between arithmetic sequences (constant difference) or geometric sequences (constant ratio)"
    )
    
    # Create input section
    st.header("Input Parameters")
    
    # Input fields in columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            help=f"The first term of the {sequence_type.lower()} sequence"
        )
        
        if sequence_type == "Arithmetic":
            common_diff = st.number_input(
                "Common Difference (d)",
                value=1.0,
                help="The difference between consecutive terms"
            )
            common_ratio = 0  # Initialize but not used
        else:  # Geometric
            common_ratio = st.number_input(
                "Common Ratio (r)",
                value=2.0,
                help="The ratio between consecutive terms"
            )
            common_diff = 0  # Initialize but not used
    
    with col2:
        num_terms = st.number_input(
            "Number of Terms (n)",
            min_value=1,
            max_value=1000,
            value=10,
            step=1,
            help="How many terms to generate (must be positive)"
        )
    
    # Add some spacing
    st.markdown("---")
    
    # Generate and display the sequence
    if st.button("Generate Sequence", type="primary") or True:  # Auto-generate on input change
        try:
            # Input validation
            if num_terms <= 0:
                st.error("Number of terms must be a positive integer.")
                return
            
            if num_terms > 1000:
                st.error("Number of terms cannot exceed 1000.")
                return
            
            # Generate the sequence based on type
            if sequence_type == "Arithmetic":
                sequence = generate_arithmetic_sequence(first_term, common_diff, num_terms)
                formula_text = f"**Formula:** aₙ = {first_term} + (n-1) × {common_diff}"
                param_name = "Common Difference"
                param_value = common_diff
                param_symbol = "d"
            else:  # Geometric
                sequence = generate_geometric_sequence(first_term, common_ratio, num_terms)
                formula_text = f"**Formula:** aₙ = {first_term} × {common_ratio}^(n-1)"
                param_name = "Common Ratio"
                param_value = common_ratio
                param_symbol = "r"
            
            if sequence:
                st.header(f"Generated {sequence_type} Sequence")
                
                # Display sequence formula
                st.markdown(formula_text)
                
                # Display sequence information
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("First Term", f"{first_term}")
                with col2:
                    st.metric(param_name, f"{param_value}")
                with col3:
                    st.metric("Number of Terms", f"{num_terms}")
                
                # Display the sequence in different formats
                tab1, tab2, tab3, tab4 = st.tabs(["List View", "Table View", "Mathematical Notation", "Sum Formula (Sₙ)"])
                
                with tab1:
                    st.subheader("Sequence as List")
                    # Format the sequence nicely
                    sequence_str = ", ".join([f"{term:g}" for term in sequence])
                    st.code(f"[{sequence_str}]")
                
                with tab2:
                    st.subheader("Sequence as Table")
                    # Create a table with term number and value
                    import pandas as pd
                    df_data = {
                        "Term (n)": list(range(1, num_terms + 1)),
                        "Value (aₙ)": sequence
                    }
                    df = pd.DataFrame(df_data)
                    st.dataframe(df, hide_index=True, width="stretch")
                
                with tab3:
                    st.subheader("Mathematical Notation")
                    st.markdown("**Sequence Terms:**")
                    # Display first few terms with their calculations
                    display_limit = min(10, num_terms)
                    for i in range(display_limit):
                        term_value = sequence[i]
                        if i == 0:
                            st.markdown(f"a₁ = {first_term} = {term_value:g}")
                        else:
                            if sequence_type == "Arithmetic":
                                st.markdown(f"a{i+1} = {first_term} + {i} × {param_value} = {term_value:g}")
                            else:  # Geometric
                                st.markdown(f"a{i+1} = {first_term} × {param_value}^{i} = {term_value:g}")
                    
                    if num_terms > display_limit:
                        st.markdown(f"... (showing first {display_limit} terms)")
                        if sequence_type == "Arithmetic":
                            st.markdown(f"a{num_terms} = {first_term} + {num_terms-1} × {param_value} = {sequence[-1]:g}")
                        else:  # Geometric
                            st.markdown(f"a{num_terms} = {first_term} × {param_value}^{num_terms-1} = {sequence[-1]:g}")
                
                with tab4:
                    st.subheader(f"Sum of First n Terms (Sₙ) - {sequence_type}")
                    
                    # Calculate sum
                    sum_sequence = sum(sequence)
                    
                    if sequence_type == "Arithmetic":
                        # Arithmetic Series Sum
                        st.markdown("**Primary Sum Formula:**")
                        st.latex(r"S_n = \frac{n}{2} \times (2a_1 + (n-1)d)")
                        
                        # Show substitution
                        st.markdown("**Substituting our values:**")
                        st.markdown(f"- n = {num_terms}")
                        st.markdown(f"- a₁ = {first_term}")
                        st.markdown(f"- d = {param_value}")
                        
                        # Step-by-step calculation
                        st.markdown("**Step-by-step calculation:**")
                        step1 = f"S_{num_terms} = {num_terms}/2 × (2×{first_term} + ({num_terms}-1)×{param_value})"
                        st.markdown(f"1. {step1}")
                        
                        inner_calc = 2 * first_term + (num_terms - 1) * param_value
                        step2 = f"S_{num_terms} = {num_terms}/2 × ({2 * first_term} + {(num_terms - 1) * param_value})"
                        st.markdown(f"2. {step2}")
                        
                        step3 = f"S_{num_terms} = {num_terms}/2 × {inner_calc}"
                        st.markdown(f"3. {step3}")
                        
                        step4 = f"S_{num_terms} = {num_terms * inner_calc / 2}"
                        st.markdown(f"4. {step4}")
                        
                        # Alternative formula
                        st.markdown("---")
                        st.markdown("**Alternative Sum Formula (using first and last term):**")
                        last_term = sequence[-1]
                        st.latex(r"S_n = \frac{n}{2} \times (a_1 + a_n)")
                        st.markdown(f"S_{num_terms} = {num_terms}/2 × ({first_term} + {last_term}) = {num_terms * (first_term + last_term) / 2:g}")
                        
                    else:  # Geometric
                        # Geometric Series Sum
                        st.markdown("**Primary Sum Formula:**")
                        if abs(param_value - 1) < 1e-10:  # r = 1
                            st.latex(r"S_n = n \times a_1 \quad \text{(when r = 1)}")
                            st.markdown("**Step-by-step calculation:**")
                            st.markdown(f"Since r = 1, all terms are equal to a₁ = {first_term}")
                            st.markdown(f"S_{num_terms} = {num_terms} × {first_term} = {sum_sequence:g}")
                        else:  # r ≠ 1
                            st.latex(r"S_n = a_1 \times \frac{1 - r^n}{1 - r} \quad \text{(when r ≠ 1)}")
                            
                            # Show substitution
                            st.markdown("**Substituting our values:**")
                            st.markdown(f"- n = {num_terms}")
                            st.markdown(f"- a₁ = {first_term}")
                            st.markdown(f"- r = {param_value}")
                            
                            # Step-by-step calculation
                            st.markdown("**Step-by-step calculation:**")
                            r_power_n = param_value ** num_terms
                            step1 = f"S_{num_terms} = {first_term} × (1 - {param_value}^{num_terms}) / (1 - {param_value})"
                            st.markdown(f"1. {step1}")
                            
                            step2 = f"S_{num_terms} = {first_term} × (1 - {r_power_n}) / ({1 - param_value})"
                            st.markdown(f"2. {step2}")
                            
                            numerator = 1 - r_power_n
                            denominator = 1 - param_value
                            step3 = f"S_{num_terms} = {first_term} × ({numerator}) / ({denominator})"
                            st.markdown(f"3. {step3}")
                            
                            step4 = f"S_{num_terms} = {first_term * numerator / denominator}"
                            st.markdown(f"4. {step4}")
                    
                    # Final result with verification
                    st.markdown("---")
                    col_sum1, col_sum2 = st.columns(2)
                    
                    with col_sum1:
                        st.metric("Sum using Formula", f"{sum_sequence:g}")
                        if sequence_type == "Arithmetic":
                            st.caption("Sₙ = n/2 × (2a₁ + (n-1)d)")
                        else:
                            if abs(param_value - 1) < 1e-10:
                                st.caption("Sₙ = n × a₁ (when r = 1)")
                            else:
                                st.caption("Sₙ = a₁(1-rⁿ)/(1-r)")
                    
                    with col_sum2:
                        st.metric("Sum by Addition", f"{sum_sequence:g}")
                        st.caption("Direct addition of all terms")
                
                # Additional sequence properties
                st.markdown("---")
                st.subheader("Sequence Properties")
                
                prop_col1, prop_col2 = st.columns(2)
                
                with prop_col1:
                    if num_terms > 1:
                        sum_sequence = sum(sequence)
                        st.metric("Sum of Terms", f"{sum_sequence:g}")
                        
                        if sequence_type == "Arithmetic":
                            formula_sum = (num_terms / 2) * (2 * first_term + (num_terms - 1) * param_value)
                            st.caption(f"Formula: Sₙ = n/2 × (2a₁ + (n-1)d) = {formula_sum:g}")
                        else:  # Geometric
                            if abs(param_value - 1) < 1e-10:
                                formula_sum = num_terms * first_term
                                st.caption(f"Formula: Sₙ = n × a₁ = {formula_sum:g}")
                            else:
                                formula_sum = first_term * (1 - param_value ** num_terms) / (1 - param_value)
                                st.caption(f"Formula: Sₙ = a₁(1-rⁿ)/(1-r) = {formula_sum:g}")
                
                with prop_col2:
                    if num_terms > 0:
                        last_term = sequence[-1]
                        st.metric("Last Term", f"{last_term:g}")
                        if sequence_type == "Arithmetic":
                            st.caption(f"Formula: aₙ = a₁ + (n-1)d")
                        else:  # Geometric
                            st.caption(f"Formula: aₙ = a₁ × r^(n-1)")
                
            else:
                st.warning("No sequence generated. Please check your inputs.")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    # Add information section
    st.markdown("---")
    if sequence_type == "Arithmetic":
        st.markdown("### About Arithmetic Sequences")
        with st.expander("Learn more about arithmetic sequences"):
            st.markdown("""
            An **arithmetic sequence** is a sequence of numbers where the difference between 
            consecutive terms is constant. This difference is called the **common difference**.
            
            **General Formula:** aₙ = a₁ + (n-1)d
            
            Where:
            - aₙ = the nth term
            - a₁ = the first term
            - n = the term number
            - d = the common difference
            
            **Sum Formula:** Sₙ = n/2 × (2a₁ + (n-1)d)
            
            **Examples:**
            - 2, 4, 6, 8, 10, ... (first term = 2, common difference = 2)
            - 5, 8, 11, 14, 17, ... (first term = 5, common difference = 3)
            - 10, 7, 4, 1, -2, ... (first term = 10, common difference = -3)
            """)
    else:  # Geometric
        st.markdown("### About Geometric Sequences")
        with st.expander("Learn more about geometric sequences"):
            st.markdown("""
            A **geometric sequence** is a sequence of numbers where each term after the first 
            is found by multiplying the previous term by a constant. This constant is called 
            the **common ratio**.
            
            **General Formula:** aₙ = a₁ × r^(n-1)
            
            Where:
            - aₙ = the nth term
            - a₁ = the first term
            - n = the term number
            - r = the common ratio
            
            **Sum Formula:** 
            - When r ≠ 1: Sₙ = a₁ × (1 - r^n) / (1 - r)
            - When r = 1: Sₙ = n × a₁
            
            **Examples:**
            - 2, 4, 8, 16, 32, ... (first term = 2, common ratio = 2)
            - 1, 3, 9, 27, 81, ... (first term = 1, common ratio = 3)
            - 100, 50, 25, 12.5, ... (first term = 100, common ratio = 0.5)
            """)

if __name__ == "__main__":
    main()
