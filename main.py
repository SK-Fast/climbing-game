def on_a_pressed():
    if player_sprite.is_hitting_tile(CollisionDirection.BOTTOM):
        player_sprite.vy = -300
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

player_sprite: Sprite = None
player_sprite = sprites.create(assets.image("""
    Player
"""), 0)
controller.move_sprite(player_sprite, 100, 0)
player_sprite.ay = 500
scene.camera_follow_sprite(player_sprite)
tiles.set_tilemap(tilemap("""
    level1
"""))
info.set_life(3)
tiles.place_on_random_tile(player_sprite, assets.tile("""
    spawn
"""))

def on_forever():
    if player_sprite.tile_kind_at(TileDirection.TOP, assets.tile("""
        spawn0
    """)):
        tiles.set_tile_at(tiles.location_in_direction(tiles.location_of_sprite(player_sprite),
                CollisionDirection.TOP),
            assets.tile("""
                transparency16
            """))
        tiles.set_wall_at(tiles.location_in_direction(tiles.location_of_sprite(player_sprite),
                CollisionDirection.TOP),
            False)
forever(on_forever)
