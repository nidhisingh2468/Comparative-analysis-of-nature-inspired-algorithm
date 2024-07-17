import streamlit as st
import pandas as pd
import plotly.express as px


def main():
    st.title("Nature Inspired Algorithms Performance Analysis")

    # Data setup for both seasons and all algorithms
    results = {
        "Kharif": {
            "Genetic": {
                "Best Profit": 46040.68,
                "Crops": {
                    "Paddy": 3182.5,
                    "Maize": 347.63,
                    "Bajra": 84.03,
                    "Arhar": 226.57,
                    "Moong": 2.18,
                    "Urad": 46.56,
                    "Groundnut": 50.45,
                    "Sesamum": 5.87,
                    "Sugarcane": 41850.59,
                },
                "Execution Time": 0.19991111755371094,
            },
            "DifferentialEvolution": {
                "Best Profit": 46769.38,
                "Crops": {
                    "Paddy": 3247.00,
                    "Maize": 433.27,
                    "Bajra": 289.90,
                    "Arhar": 246.13,
                    "Moong": 2.29,
                    "Urad": 69.80,
                    "Groundnut": 65.47,
                    "Sesamum": 8.53,
                    "Sugarcane": 42406.98,
                },
                "Execution Time": 0.2916731834411621,
            },
            "ParticleSwarmOptimization": {
                "Best Profit": 46401.16,
                "Crops": {
                    "Paddy": 3247.01,
                    "Maize": 433.27,
                    "Bajra": 289.90,
                    "Arhar": 246.13,
                    "Moong": 2.29,
                    "Urad": 69.80,
                    "Groundnut": 65.48,
                    "Sesamum": 8.53,
                    "Sugarcane": 42406.98,
                },
                "Execution Time": 0.19247984886169434,
            },
            "EvolutionaryProgramming": {
                "Best Profit": 46001.75,
                "Crops": {
                    "Paddy": 805.75,
                    "Maize": 133.59,
                    "Bajra": 55.81,
                    "Arhar": 224.95,
                    "Moong": 2.11,
                    "Urad": 27.38,
                    "Groundnut": 44.14,
                    "Sesamum": 6.24,
                    "Sugarcane": 42406.98,
                },
                "Execution Time": 0.008893489837646484,
            },
        },
        "Rabi": {
            "Genetic": {
                "Best Profit": 9910.37,
                "Crops": {
                    "Wheat": 7848.49,
                    "Barley": 88.05,
                    "Gram": 190.75,
                    "R & M": 478.26,
                    "Lentil": 130.59,
                    "Potato": 861.29,
                },
                "Execution Time": 0.016266584396362305,
            },
            "DifferentialEvolution": {
                "Best Profit": 10004.06,
                "Crops": {
                    "Wheat": 7931.98,
                    "Barley": 124.4,
                    "Gram": 203.35,
                    "R & M": 550.07,
                    "Lentil": 161.0,
                    "Potato": 1033.26,
                },
                "Execution Time": 0.19333124160766602,
            },
            "ParticleSwarmOptimization": {
                "Best Profit": 9800.71,
                "Crops": {
                    "Wheat": 7931.98,
                    "Barley": 0.0,
                    "Gram": 203.35,
                    "R & M": 550.07,
                    "Lentil": 161.0,
                    "Potato": 1033.26,
                },
                "Execution Time": 0.13570046424865723,
            },
            "EvolutionaryProgramming": {
                "Best Profit": 9387.80,
                "Crops": {
                    "Wheat": 7931.98,
                    "Barley": 84.97,
                    "Gram": 42.29,
                    "R & M": 550.07,
                    "Lentil": 104.07,
                    "Potato": 732.63,
                },
                "Execution Time": 0.005026102066040039,
            },
        },
    }

    # User inputs via form
    with st.form("input_form"):
        season = st.selectbox("Select the season:", ["Kharif", "Rabi"])
        algorithm = st.selectbox(
            "Select the algorithm:",
            [
                "Genetic",
                "Differential Evolution",
                "Particle Swarm Optimization",
                "Evolutionary Programming",
            ],
        )
        submitted = st.form_submit_button("Submit")

    if submitted:
        algorithm_results = results[season][algorithm]
        st.subheader(f"Results for {season} crop using {algorithm}:")
        st.write(f"**Best Profit:** {algorithm_results['Best Profit']}")
        st.write(f"**Execution Time:** {algorithm_results['Execution Time']} seconds")

        # Display crop data in a table
        crop_data = pd.DataFrame(
            list(algorithm_results["Crops"].items()), columns=["Crop", "Net Revenue"]
        )
        st.table(crop_data)

        # Create and display a bar chart for crop revenues
        fig = px.bar(
            crop_data,
            x="Crop",
            y="Net Revenue",
            title=f"Net Revenue for {season} crop using {algorithm}",
        )
        st.plotly_chart(fig)

        # Additional graph for comparative analysis across all algorithms for the season
        crop_comparison_data = []
        for alg, data in results[season].items():
            for crop, revenue in data["Crops"].items():
                crop_comparison_data.append(
                    {"Algorithm": alg, "Crop": crop, "Revenue": revenue}
                )

        df_crop_comparison = pd.DataFrame(crop_comparison_data)
        fig2 = px.bar(
            df_crop_comparison,
            x="Crop",
            y="Revenue",
            color="Algorithm",
            title=f"Comparison of Revenue by Crop across Algorithms for {season} Season",
        )
        st.plotly_chart(fig2)

        # Graph for comparative analysis of execution time across all algorithms for the season
        exec_time_comparison_data = []
        for alg, data in results[season].items():
            exec_time_comparison_data.append(
                {"Algorithm": alg, "Execution Time": data["Execution Time"]}
            )

        df_exec_time_comparison = pd.DataFrame(exec_time_comparison_data)
        fig3 = px.bar(
            df_exec_time_comparison,
            x="Algorithm",
            y="Execution Time",
            title=f"Comparison of Execution Time across Algorithms for {season} Season",
        )
        st.plotly_chart(fig3)

    # CSS for background
    st.markdown(
        """
        <style>
        .reportview-container {
            background: url('');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
