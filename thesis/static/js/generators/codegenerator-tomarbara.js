
            Blockly.Python['tomarbara'] = function(block) {
              var value_to_input = Blockly.Python.valueToCode(block, 'to_input', Blockly.Python.ORDER_ATOMIC);
              // TODO: Assemble JavaScript into code variable.
              var code = 'tomarbara('+value_to_input+')';
              // TODO: Change ORDER_NONE to the correct strength.
              return [code, Blockly.Python.ORDER_NONE];
            };
        