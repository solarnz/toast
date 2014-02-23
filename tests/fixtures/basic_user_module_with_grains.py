def main(grains):
    states = []
    if grains.get('vim', False):
        states.append('vim')

    return {
        'states': states,
        'pillars': {}
    }
