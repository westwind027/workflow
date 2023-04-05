from barfi import Block

noop_block=Block(name='Noop')
noop_block.add_option(name='display-option1', type='display', value='input transform str:')
noop_block.add_option(name='paratrans',type='input')
noop_block.add_output(name='Output')
noop_block.add_input(name='Input')
def noop_block_func(self):
  input_1_value = self.get_interface(name='Input')
  paratrans_value = self.get_option(name='paratrans')
  txt = "state:\n- id: helloword\n  type:noop\n  transform:\n    {trans}"
  out_1_value = txt.format(trans=paratrans_value)
  if isinstance(input_1_value, str):
    out_2_value = [input_1_value,out_1_value]
  elif isinstance(input_1_value, list):
    out_2_value = input_1_value.append(out_1_value)
  else:
    out_2_value = "error"
  self.set_interface(name='Output', value=out_2_value)
  self.set_state(key="out",value=out_2_value)


noop_block.add_compute(noop_block_func)