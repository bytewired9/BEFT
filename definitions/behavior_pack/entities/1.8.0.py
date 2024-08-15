# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

index = {
    "format_version": "1.8.0",
    "do_not_upgrade": {}
}
description = {
    "minecraft:identifier": "[STR]",
    "minecraft:is_experimental": "[BOOL]/false",
    "minecraft:is_summonable": "[BOOL]/false",
    "minecraft:runtime_identifier": "[STR]",
    "minecraft:spawn_egg": "[BOOL]/false",
}

attributes = {
    "minecraft:attack": {
        "damage": ["[FLOAT]", "[FLOAT]"],
        "effect_duration": "[FLOAT]/0.0",
        "effect_name": "[STR]"
    },
    "minecraft:spell_effects": {
        "add_effects": "[STR]",
        "remove_effects": "[STR]",
    },
    "minecraft:strength": {
        "value": "[INT]/1",
        "max": "[INT]/5"
    }
}

properties = {
    "minecraft:ambient_sound_interval": {
        "value": "[FLOAT]/16.0",
        "range": "[FLOAT]/8.0"
    },
    "minecraft:can_climb": {},
    "minecraft:can_fly": {},
    "minecraft:can_power_jump": {},
    "minecraft:collision_box": {
        "width": "[FLOAT]/1.0",
        "height": "[FLOAT]/1.0"
    },
    "minecraft:color": {
        "value": "[INT]/0"
    },
    "minecraft:color2": {
        "value": "[INT]/0"
    },
    "minecraft:default_look_angle": {
        "value": "[FLOAT]"
    },
    "minecraft:equipment": {
        "slot_drop_chance": "[STR]",
        "table": "[STR]"
    },
    "minecraft:fire_immune": {},
    "minecraft:floats_in_liquid": {},
    "minecraft:flying_speed": {
        "value": "[FLOAT]/0.02"
    },
    "minecraft:foot_size": {
        "value": "[FLOAT]/0.5"
    },
    "minecraft:friction_modifier": {
        "value": "[FLOAT]/1.0"
    },
    "minecraft:ground_offset": {
        "value": "[FLOAT]/0.0"
    },
    "minecraft:input_ground_controlled": {},
    "minecraft:is_baby": {},
    "minecraft:is_charged": {},
    "minecraft:is_dyeable": {
        "interact_text": "[STR]"
    },
    "minecraft:is_ignited": {},
    "minecraft:is_saddled": {},
    "minecraft:is_shaking": {},
    "minecraft:is_sheared": {},
    "minecraft:is_stackable": {},
    "minecraft:is_tamed": {},
    "minecraft:item_controllable": {
        "control_items": "[STR]"
    },
    "minecraft:loot": {
        "table": "[STR]"
    },
    "minecraft:mark_variant": {
        "value": "[INT]/0"
    },
    "minecraft:push_through": {
        "value": "[FLOAT]/0.0"
    },
    "minecraft:scale": {
        "value": "[FLOAT]/1.0"
    },
    "minecraft:sound_volume": {
        "value": "[FLOAT]/1.0"
    },
    "minecraft:type_family": {
        "family": "[STR]"
    },
    "minecraft:variant": {
        "value": "[INT]/0"
    },
    "minecraft:walk_animation_speed": {
        "value": "[FLOAT]/1.0"
    }
}
