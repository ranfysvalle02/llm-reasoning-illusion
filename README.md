![](https://www.k2view.com/hubfs/Robot%20thinker.jpg)

**The Illusion of Reasoning**

The illusion of reasoning in LLMs stems from their ability to generate coherent and contextually relevant text. When presented with a prompt or question, LLMs can produce responses that appear to be the result of logical thought. However, this is primarily due to their probabilistic nature and the fact that they have been trained on vast amounts of text data. LLMs essentially learn patterns and associations within this data, allowing them to predict the most likely next word or phrase in a given context.

**Wozniak’s Perspective on Intelligence and Reasoning**

An interesting point raised by Steve Wozniak in from [Hackers Wanted - 2009](https://youtube.com/clip/UgkxNjTUlN1Tpt4ZRlQkyJ6Jd0hUdhFXuDE4?si=8Tc_u3ES-ib1xLV4) critiques the way we often define intelligence:

*“So, we don't teach thinking as much as we teach, you know, rigorous rote. And intelligence is not defined as somebody having a brain that can think and think and consider all the possibilities and come up with the best solution. Oh no no! Intelligence is saying the exact same things as everyone else. You read the same newspaper articles. You watched the same news shows. You read the same books. And now you can say exactly the same things about how the world works. So you all know you're in a group. It's almost like a religion. And we're all the same. And we're intelligent because I say it and you say it. And you're intelligent so I'm intelligent. And we never really have a real good way of measuring 'are you really thinking?' and putting it together and coming up with your own solutions. No. We don't define that as intelligent. We often define it as dumb.”*

This insight highlights a critical question for LLMs: Can we teach models to truly "think" in diverse and creative ways, or will they simply mimic societal norms and patterns they've been trained on?

**Understanding Reasoning**

Reasoning, at its core, involves the ability to draw conclusions or make inferences based on given information or evidence. It requires the application of logic, critical thinking, and problem-solving skills. 

Some types of reasoning:
* **Deductive Reasoning:** Moving from general principles to specific conclusions (e.g., "All men are mortal. Socrates is a man. Therefore, Socrates is mortal.")
* **Inductive Reasoning:** Drawing general conclusions from specific observations (e.g., "I've seen several red cars today. Red cars must be popular.")
* **Abductive Reasoning:** Inferring the most likely explanation for an observation (e.g., "The grass is wet. It must have rained.")
* **Analogical Reasoning:** Identifying similarities between situations (e.g., "A virus attacking a computer is like an illness attacking a human body.")
* **Causal Reasoning:** Understanding cause-and-effect relationships (e.g., "Eating unhealthy foods can lead to weight gain.")

While LLMs can mimic some of these forms through pre-learned patterns, true reasoning requires a deliberate cognitive framework, which they lack.

**A deliberate cognitive framework** is a structured mental approach that involves:

* **Conscious thought:** Deliberately considering information and making decisions.
* **Critical analysis:** Evaluating information, identifying strengths, weaknesses, and biases.
* **Problem-solving:** Applying strategies to overcome challenges and find solutions.
* **Logical reasoning:** Using rules and principles to draw valid conclusions.

In essence, it's a way of thinking that goes beyond automatic responses or pre-learned patterns. It requires active engagement with information, the ability to make informed judgments, and the capacity to solve problems creatively.

**Imagine a detective solving a crime.**

* **A deliberate cognitive framework** would involve:
    * Carefully examining all the evidence.
    * Considering different theories and possibilities.
    * Using logic to connect the dots and identify the culprit.
    * Being open to new information and adjusting their thinking as needed.

* **In contrast, a simple pattern-matching system** might:
    * Look for similarities between the current case and previous ones.
    * Suggest a solution based on past experiences.
    * But it might miss important details or fail to consider alternative explanations.

**Implementing Reasoning in LLMs via Reinforcement Learning**
   * **Reward-based learning:** Training LLMs to make decisions based on rewards or punishments.
   * **Reasoning as a game:** Formulating reasoning tasks as games where the LLM learns to make optimal choices.
   * **Example:** Training an LLM to play a reasoning game like chess.

_NOTE: At the core of [OpenAI](https://openai.com/index/learning-to-reason-with-llms/) o1's capabilities is its large-scale reinforcement learning algorithm. This approach teaches the model how to think productively by encouraging it to generate chains of thought that lead to correct solutions._


**Python Example: Strawberry Problem Solved with GPT3.5 + CoT "Reasoning"**

```python

from openai import AzureOpenAI

# Define constants
AZURE_OPENAI_ENDPOINT = ""
AZURE_OPENAI_API_KEY = "" 
az_client = AzureOpenAI(azure_endpoint=AZURE_OPENAI_ENDPOINT,api_version="2023-07-01-preview",api_key=AZURE_OPENAI_API_KEY)
ai_response = az_client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {"role": "user", "content": "Count the occurrences of the letter 'r' in the word 'strawberry'."},
    ]
)
print("gpt-35-turbo")
print(ai_response.choices[0].message.content)
print("------------")
ai_response = az_client.chat.completions.create(
    model="gpt-35-turbo",
    messages=[
        {"role": "user", "content": "Count the occurrences of the letter 'r' in the word 'strawberry'."},
        {"role": "system", "content": """         
<chain of thought>
EXAMPLE: Count the occurrences of the letter 'p' in the word 'apple'.
To determine the number of occurrences of the letter 'p' in the word 'apple', we scan through the word letter by letter: 
        'a' (0), 'p' (1), 'p' (2), 'l' (0), 'e' (0). 
Therefore, the letter 'p' appears 2 times.
</chain of thought>
IMPORTANT! USE ABOVE CHAIN OF THOUGHT TO GENERATE YOUR RESPONSE!
"""}
    ]
)
print("gpt-35-turbo with CoT")
print(ai_response.choices[0].message.content)
print("------------")

```

**Output**

```
gpt-35-turbo
There are 2 occurrences of the letter 'r' in the word 'strawberry'.
------------
gpt-35-turbo with CoT
To determine the number of occurrences of the letter 'r' in the word 'strawberry', we scan through the word letter by letter:

- 's' (0)
- 't' (0)
- 'r' (1)
- 'a' (0)
- 'w' (0)
- 'b' (0)
- 'e' (0)
- 'r' (2)
- 'r' (3)
- 'y' (0)

Therefore, the letter 'r' appears 3 times in the word 'strawberry'.
------------
```

**Challenges and Future Directions**

* **Complexity:** Reasoning is a complex cognitive process that involves multiple interconnected components.
* **Data scarcity:** Acquiring sufficient data for training LLMs on reasoning tasks can be challenging.
* **Evaluation:** Developing effective metrics to evaluate the reasoning capabilities of LLMs is an ongoing area of research.
* **Bias and fairness:** Ensuring that LLMs reason in a fair and unbiased manner is non-trivial.

**Resources**

[Why can't LLM's count?](https://github.com/ranfysvalle02/strawberry-ai)
