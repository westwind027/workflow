from barfi import Block

event_block=Block(name='Event Listener')
event_block.add_option(name='display-option1', type='display', value='Choose the listentype:')
event_block.add_option(name='listentype',type='select',items=['event', 'eventsAnd','eventsXor'],value='event')
event_block.add_option(name='display-option2', type='display', value='Input eventype:')
event_block.add_option(name='eventype',type='input')
event_block.add_output(name='Output')
def event_block_func(self):
  input_1_value = self.get_option(name='eventype')
  select_1_value = self.get_option(name='listentype')
  out_1_value = "Start:\n  type:{0}\n  events:\n    type:{1}\n  state:".format(select_1_value, input_1_value)
  self.set_interface(name='Output', value=out_1_value)

event_block.add_compute(event_block_func)