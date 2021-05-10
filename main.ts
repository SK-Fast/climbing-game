controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    if (player_sprite.isHittingTile(CollisionDirection.Bottom)) {
        player_sprite.vy = -300
    }
    
})
let player_sprite : Sprite = null
player_sprite = sprites.create(assets.image`
    Player
`, 0)
controller.moveSprite(player_sprite, 100, 0)
player_sprite.ay = 500
scene.cameraFollowSprite(player_sprite)
tiles.setTilemap(tilemap`
    level1
`)
info.setLife(3)
tiles.placeOnRandomTile(player_sprite, assets.tile`
    spawn
`)
forever(function on_forever() {
    if (player_sprite.tileKindAt(TileDirection.Top, assets.tile`
        spawn0
    `)) {
        tiles.setTileAt(tiles.locationInDirection(tiles.locationOfSprite(player_sprite), CollisionDirection.Top), assets.tile`
                transparency16
            `)
        tiles.setWallAt(tiles.locationInDirection(tiles.locationOfSprite(player_sprite), CollisionDirection.Top), false)
    }
    
})
