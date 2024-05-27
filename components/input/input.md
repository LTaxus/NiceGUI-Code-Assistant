# ui._input_

This element is based on Quasar's [QInput](https://quasar.dev/vue-components/input) component.

The on_change event is called on every keystroke and the value updates accordingly. If you want to wait until the user confirms the input, you can register a custom event callback, e.g. ui.input(...).on('keydown.enter', ...) or ui.input(...).on('blur', ...).

You can use the validation parameter to define a dictionary of validation rules. The key of the first rule that fails will be displayed as an error message.

Note about styling the input: Quasar's QInput component is a wrapper around a native input element. This means that you cannot style the input directly, but you can use the input-class and input-style props to style the native input element. See the "Style" props section on the [QInput](https://quasar.dev/vue-components/input) documentation for more details.

label: displayed label for the text input
placeholder: text to show if no value is entered
value: the current value of the text input
password: whether to hide the input (default: False)
password_toggle_button: whether to show a button to toggle the password visibility (default: False)
on_change: callback to execute when the value changes
autocomplete: optional list of strings for autocompletion
validation: dictionary of validation rules, e.g. {'Too long!': lambda value: len(value) < 3}


```python
from nicegui import ui

ui.input(label='Text', placeholder='start typing',
         on_change=lambda e: result.set_text('you typed: ' + e.value),
         validation={'Input too long': lambda value: len(value) < 20})
result = ui.label()

ui.run()
```

## Autocompletion

The `autocomplete` feature provides suggestions as you type, making input easier and faster. The parameter `options` is a list of strings that contains the available options that will appear.

```python
from nicegui import ui

options = ['AutoComplete', 'NiceGUI', 'Awesome']
ui.input(label='Text', placeholder='start typing', autocomplete=options)

ui.run()
```

## Clearable

The `clearable` prop from [Quasar](https://quasar.dev/) adds a button to the input that clears the text.

```python
from nicegui import ui

i = ui.input(value='some text').props('clearable')
ui.label().bind_text_from(i, 'value')

ui.run()
```

## Styling

Quasar has a lot of [props to change the appearance](https://quasar.dev/vue-components/input). It is even possible to style the underlying input with `input-style` and `input-class` props and use the provided slots to add custom elements.

```python
from nicegui import ui

ui.input(placeholder='start typing').props('rounded outlined dense')
ui.input('styling', value='some text') \
    .props('input-style="color: blue" input-class="font-mono"')
with ui.input(value='custom clear button').classes('w-64') as i:
    ui.button(color='orange-8', on_click=lambda: i.set_value(None), icon='delete') \
        .props('flat dense').bind_visibility_from(i, 'value')

ui.run()
```


