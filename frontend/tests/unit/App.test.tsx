import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import App from '../../src/App';

describe('App', () => {
  // Test setup placeholder. PASS
  it('renders the ODEN heading', () => {
    render(<App />);

    expect(screen.getByRole('heading', { name: 'ODEN' })).toBeInTheDocument();
  });

  // Test setup placeholder.  FAIL
  it('Fail case', () => {
    render(<App />);
    const temp = 3;
    expect(1 + 1).toBe(temp);
  });
});
