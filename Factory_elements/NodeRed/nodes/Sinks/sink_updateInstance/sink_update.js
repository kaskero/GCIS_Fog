const fs = require('fs');
const yaml = require('js-yaml');


module.exports = function(RED) {
    function SinkUpdateInstance(config) {
        RED.nodes.createNode(this,config);
        this.endpoint = config.endpoint;
        var node = this;
        
        node.on('input', function(msg) {

            let data = { sink: {
                        image: "gcr.io/clusterekaitz/appfil1:sink",
                        container_name: "sink",
                        ports: ["8080:8080"],
                        environment: ["SERVICE_TYPE=updateProductInstance"]
                    }
            };

            let previousComponent = yaml.safeLoad(msg.payload);

            let join = Object.assign(previousComponent, data);

            let yamlStr = yaml.safeDump(join);
            fs.writeFileSync('def-sink-update.yml', yamlStr, 'utf8');
            msg.payload = yamlStr;
            node.send(msg);
        });
    }
    RED.nodes.registerType("Update instance",SinkUpdateInstance);
}



