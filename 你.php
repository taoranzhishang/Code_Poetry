/**
* I love three things in this world.
* Sun, moon and you.
* Sun for morning, moon for night, and you forever.
*/
class LoveThreeThings extends Me
{
    const loveFirstThings  = 'Sun';
    const loveSecondThings = 'Moon';
    const loveThirdThings  = 'You';

    public function MyLove()
    {
        return 'I Love' . self::loveThirdThings . 'forever. Never change!';
    }
}