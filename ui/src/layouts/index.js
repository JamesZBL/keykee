import styles from './index.css';

function BasicLayout(props) {
  return (
    <div className={styles.normal}>
      <h1 className={styles.title}>Hey! Welcome to Keykee!</h1>
      <h3 className={styles.title}>Here is your key statistic.</h3>
      { props.children }
    </div>
  );
}

export default BasicLayout;
