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

def main():
    # Set page title and header
    st.set_page_config(
        page_title="Arithmetic Sequence Generator",
        page_icon="🔢",
        layout="centered"
    )
    
    st.title("🔢 Arithmetic Sequence Generator")
    st.markdown("Generate arithmetic sequences by specifying the first term, common difference, and number of terms.")
    
    # Create input section
    st.header("Input Parameters")
    
    # Input fields in columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        first_term = st.number_input(
            "First Term (a₁)",
            value=1.0,
            help="The first term of the arithmetic sequence"
        )
        
        common_diff = st.number_input(
            "Common Difference (d)",
            value=1.0,
            help="The difference between consecutive terms"
        )
    
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
            
            # Generate the sequence
            sequence = generate_arithmetic_sequence(first_term, common_diff, num_terms)
            
            if sequence:
                st.header("Generated Arithmetic Sequence")
                
                # Display sequence formula
                st.markdown(f"**Formula:** aₙ = {first_term} + (n-1) × {common_diff}")
                
                # Display sequence information
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("First Term", f"{first_term}")
                with col2:
                    st.metric("Common Difference", f"{common_diff}")
                with col3:
                    st.metric("Number of Terms", f"{num_terms}")
                
                # Display the sequence in different formats
                tab1, tab2, tab3 = st.tabs(["List View", "Table View", "Mathematical Notation"])
                
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
                    st.dataframe(df, hide_index=True, use_container_width=True)
                
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
                            st.markdown(f"a{i+1} = {first_term} + {i} × {common_diff} = {term_value:g}")
                    
                    if num_terms > display_limit:
                        st.markdown(f"... (showing first {display_limit} terms)")
                        st.markdown(f"a{num_terms} = {first_term} + {num_terms-1} × {common_diff} = {sequence[-1]:g}")
                
                # Additional sequence properties
                st.markdown("---")
                st.subheader("Sequence Properties")
                
                prop_col1, prop_col2 = st.columns(2)
                
                with prop_col1:
                    if num_terms > 1:
                        sum_sequence = sum(sequence)
                        st.metric("Sum of Terms", f"{sum_sequence:g}")
                        
                        # Sum formula: S_n = n/2 * (2a + (n-1)d)
                        formula_sum = (num_terms / 2) * (2 * first_term + (num_terms - 1) * common_diff)
                        st.caption(f"Formula: Sₙ = n/2 × (2a₁ + (n-1)d) = {formula_sum:g}")
                
                with prop_col2:
                    if num_terms > 0:
                        last_term = sequence[-1]
                        st.metric("Last Term", f"{last_term:g}")
                        st.caption(f"Formula: aₙ = a₁ + (n-1)d")
                
            else:
                st.warning("No sequence generated. Please check your inputs.")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    
    # Add information section
    st.markdown("---")
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

if __name__ == "__main__":
    main()
