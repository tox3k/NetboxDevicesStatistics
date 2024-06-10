class NetboxItem:
    def __init__(
            self,
            id: int,
            url: str,
            display: str,
            name: str,
            device_type: dict,
            role: dict,
            tenant: dict,
            platform: dict,
            serial: str,
            asset_tag: str,
            site: dict,
            location: dict,
            rack: dict,
            position: int,
            face: dict,
            latitude: float,
            longitude: float,
            parent_device: dict,
            status: dict,
            airflow: dict,
            primary_ip: dict,
            primary_ip4: dict,
            primary_ip6: dict,
            oob_ip: dict,
            cluster: dict,
            virtual_chassis: dict,
            vc_position: int,
            vc_priority: int,
            description: str,
            comments: str,
            config_template: str,
            config_context: dict,
            local_context_data: dict,
            tags: list,
            custom_fields: dict,
            created: str,
            last_updated: str,
            console_port_count: int,
            console_server_port_count: int,
            power_port_count: int,
            power_outlet_count: int,
            interface_count: int,
            front_port_count: int,
            rear_port_count: int,
            device_bay_count: int,
            module_bay_count: int,
            inventory_item_count: int
            ) -> None:
            
            self.id = id
            self.url = url
            self.display = display
            self.name = name
            self.device_type = device_type
            self.role = role
            self.tenant = tenant
            self.platform = platform
            self.serial = serial
            self.asset_tag = asset_tag
            self.site = site
            self.location = location
            self.rack = rack
            self.position = position
            self.face = face
            self.latitude = latitude
            self.longitude = longitude
            self.parent_device = parent_device
            self.status = status
            self.airflow = airflow
            self.primary_ip = primary_ip
            self.primary_ip4 = primary_ip4
            self.primary_ip6 = primary_ip6
            self.oob_ip = oob_ip
            self.cluster = cluster
            self.virtual_chassis = virtual_chassis
            self.vc_position = vc_position
            self.vc_priority = vc_priority
            self.description = description
            self.comments = comments
            self.config_template = config_template
            self.config_context = config_context
            self.local_context_data = local_context_data
            self.tags = tags
            self.custom_fields = custom_fields
            self.created = created
            self.last_updated = last_updated
            self.console_port_count = console_port_count
            self.console_server_port_count = console_server_port_count
            self.power_port_count = power_port_count
            self.power_outlet_count = power_outlet_count
            self.interface_count = interface_count
            self.front_port_count = front_port_count
            self.rear_port_count = rear_port_count
            self.device_bay_count = device_bay_count
            self.module_bay_count = module_bay_count
            self.inventory_item_count = inventory_item_count
    
    def __str__(self) -> str:
        res = []
        for k, v in self.__dict__.items():
            res.append(f'{k} : {v}')
        
        return '\n'.join(res)
        