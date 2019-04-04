//weater block start
Blockly.Blocks['weather'] = {
      init: function() {
        this.appendDummyInput()
        .appendField(new Blockly.FieldLabel('weather api'));//label
        this.setOutput(true, 'String');
        //this.setPreviousStatement(true, 'Action');
        this.setColour(160);
      }
    }
//weather block end

//motor block start
    Blockly.Blocks['motor-on'] = {
      init: function() {
        this.appendDummyInput()
        .appendField(new Blockly.FieldLabel('motor on'));//label 
        //this.setOutput(true, 'String');
        this.setPreviousStatement(true, 'Action');
        this.setColour(60);
      }
    }

    Blockly.Blocks['motor-off'] = {
      init: function() {
        this.appendDummyInput()
        .appendField(new Blockly.FieldLabel('motor off'));
        //this.setOutput(true, 'String');
        this.setPreviousStatement(true, 'Action');
        this.setColour(20);
      }
    }
//motor block end

//lower sensor block start
Blockly.Blocks['l-sensor'] = {
    init: function() {
        this.appendDummyInput()
        .appendField(new Blockly.FieldLabel('lower sensor'));
        this.setOutput(true, 'Number');
        //this.setPreviousStatement(true, 'Action');
        this.setColour(20);
    }
}
//lower sensor block endfghfg


//OTEDST sensor block start
Blockly.Blocks['OTEDST'] = {
	init: function() {
		this.appendDummyInput()
		.appendField(new Blockly.FieldLabel('OTEDST'));
		this.setOutput(true, 'Number');
		this.setColour(20);
	}
}
//OTEDST sensor block end

//albert000 sensor block start
Blockly.Blocks['albert000'] = {
	init: function() {
		this.appendDummyInput()
		.appendField(new Blockly.FieldLabel('albert000'));
		this.setOutput(true, 'Number');
		this.setColour(20);
	}
}
//albert000 sensor block end

//albert000 sensor block start
Blockly.Blocks['albert000'] = {
	init: function() {
		this.appendDummyInput()
		.appendField(new Blockly.FieldLabel('albert000'));
		this.setOutput(true, 'Number');
		this.setColour(20);
	}
}
//albert000 sensor block end

//albert098 sensor block start
Blockly.Blocks['albert098'] = {
	init: function() {
		this.appendDummyInput()
		.appendField(new Blockly.FieldLabel('albert098'));
		this.setOutput(true, 'Number');
		this.setColour(20);
	}
}
//albert098 sensor block end

//dzbz123 sensor block start
Blockly.Blocks['dzbz123'] = {
	init: function() {
		this.appendDummyInput()
		.appendField(new Blockly.FieldLabel('dzbz123'));
		this.setOutput(true, 'Number');
		this.setColour(20);
	}
}
//dzbz123 sensor block end