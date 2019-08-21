[RequireComponent (typeof(Rigidbody))]
 public class Movement : MonoBehaviour {
 
     public float movementSpeed = 5.0f;
     public float clockwise = 1000.0f;
     public float counterClockwise = -5.0f;
 
     void Start () {
         
     }
     
     void Update () {
         if(Input.GetKey(KeyCode.W)) {
             transform.position += Vector3.forward * Time.deltaTime * movementSpeed;
         }
         else if(Input.GetKey(KeyCode.S)) {
             rigidbody.position += Vector3.back * Time.deltaTime * movementSpeed;
         }
         else if(Input.GetKey(KeyCode.A)) {
             rigidbody.position += Vector3.left * Time.deltaTime * movementSpeed;
         }
         else if(Input.GetKey(KeyCode.D)) {
             rigidbody.position += Vector3.right * Time.deltaTime * movementSpeed;
         }
 
         if(Input.GetKey(KeyCode.E)) {
             transform.Rotate(0, Time.deltaTime * clockwise, 0);
         }
         else if(Input.GetKey(KeyCode.Q)) {
             transform.Rotate(0, Time.deltaTime * counterClockwise, 0);
         }
     }
 }