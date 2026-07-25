Create reusable prompts with variable placeholders using PromptTemplate:

from langchain_core.prompts import PromptTemplate

prompt_template_str = "... {input_text} ..."
prompt_template = PromptTemplate.from_template(prompt_template_str)
prompt = prompt_template.format(input_text="your value")
