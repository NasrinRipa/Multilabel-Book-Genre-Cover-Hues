import gradio as gr
import onnxruntime as rt
from transformers import AutoTokenizer
import torch, json

tokenizer = AutoTokenizer.from_pretrained("distilroberta-base")

with open("color_types_encoded50.json", "r") as fp:
  encode_color_types = json.load(fp)

colors = list(encode_color_types.keys())

# Set the providers parameter to use CPUExecutionProvider as fallback
#providers = ['CPUExecutionProvider']
#inf_session = rt.InferenceSession('rainbow-genre-cover-classifier-quantized.onnx', providers=providers)

inf_session = rt.InferenceSession('rainbow-genre-cover-classifier-quantized.onnx')
input_name = inf_session.get_inputs()[0].name
output_name = inf_session.get_outputs()[0].name


#inf_session = rt.InferenceSession('book-classifier-quantized.onnx')
#input_name = inf_session.get_inputs()[0].name
#output_name = inf_session.get_outputs()[0].name

def classify_rainbow_cover_color(description_and_genres):
  input_ids = tokenizer(description_and_genres)['input_ids'][:512]
  logits = inf_session.run([output_name], {input_name: [input_ids]})[0]
  logits = torch.FloatTensor(logits)
  probs = torch.sigmoid(logits)[0]
  return dict(zip(colors, map(float, probs))) 

label = gr.outputs.Label(num_top_classes=10)
iface = gr.Interface(fn=classify_rainbow_cover_color, inputs="text", outputs=label)
iface.launch(inline=False)



