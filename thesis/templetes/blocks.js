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


        
            Blockly.Blocks['kihdis1'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('kihdis1');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['soil_moisture_sensor::3.22::1.22::Digonta3'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('soil_moisture_sensor::3.22::1.22::Digonta3');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['soil_moisture_sensor_3.22_1.22_Avee4'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('soil_moisture_sensor_3.22_1.22_Avee4');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['soil_moisture_sensor_2_33_1_22_Arif5'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('soil_moisture_sensor_2_33_1_22_Arif5');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['soil_moisture_sensor_3_22_2_111_User'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('soil_moisture_sensor_3_22_2_111_User');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['Motor_actuator_longi_actuator_lati_Sayeed'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('Motor_actuator_longi_actuator_lati_Sayeed');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['Motor_actuator_longi_actuator_lati_User'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('Motor_actuator_longi_actuator_lati_User');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['Motor_actuator_longi_actuator_lati_New User'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('Motor_actuator_longi_actuator_lati_New User');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['device_name_actuator_longi_actuator_lati_owner_name'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('device_name_actuator_longi_actuator_lati_owner_name');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        
            Blockly.Blocks['Labtest_2_33_1_22_LAB'] = {
            init: function() {
            this.appendValueInput("to_input")
            .setCheck(null)
            .appendField('Labtest_2_33_1_22_LAB');
            this.setOutput(true, null);
            this.setColour(230);
            this.setTooltip("");
            this.setHelpUrl("");
      }
    };
        