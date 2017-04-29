

class PlayerNewsItem:
    def __init__(self, caption, description, published_at, updated_at, source_update_id, source_id, source_player_id,
                 first_name, last_name, position, team, date, priority, headline, injury):
        self.caption = caption
        self.description = description
        self.published_at = published_at
        self.updated_at = updated_at
        self.source_update_id = source_update_id
        self.source_id = source_id
        self.source_player_id = source_player_id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.team = team
        self.date = date
        self.priority = priority
        self.headline = headline
        self.injury = injury
