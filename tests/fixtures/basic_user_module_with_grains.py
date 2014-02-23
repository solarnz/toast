def main(grains):
    states = []
    pillars = {}
    if grains.get('vim', False):
        states.append('vim')
        pillars['vim'] = 'gvim'

    return {
        'states': states,
        'pillars': pillars
    }
