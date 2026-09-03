from agent import run_agent


def main():
    question = input("Enter a prediction-market question: ").strip() #in case there is nothing
    print("\n The forecasting agent is running...\n")
    result = run_agent(question)
    print("\n The final forecast by the agent is...:")
    print(result)

if __name__ == "__main__":
    main()
